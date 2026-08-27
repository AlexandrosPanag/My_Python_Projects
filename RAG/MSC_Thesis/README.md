# RAG Chatbot System — Code Summary

> **Project:** Master's Thesis — Hellenic Mediterranean University (HMU), Informatics Engineering
> **Author:** Alexandros Panagiotakopoulos · Academic ID: MTP333
> **License:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
> **Semester:** Winter 2025–2026

A Retrieval-Augmented Generation (RAG) chatbot for the **Open eClass LMS**, served via a local Flask web interface. The two files (`TINYLLAMARAG.py` and `QWENRAG.py`) are **identical in architecture** — the only difference is the underlying generative AI fallback model (TinyLlama vs. Qwen).

---

## Architecture Overview

The system is built around a **5-step fallback pipeline**:

| Step | Source | Triggered when |
|------|--------|---------------|
| 1 | 📄 Document RAG | Always (primary) |
| 2 | ❓ FAQ Knowledge Base | Document confidence < 45% |
| 3 | 🤖 AI Language Model (TinyLlama / Qwen) | No FAQ match found |
| 4 | 🔍 Open eClass Docs Search Link | AI unavailable or fails |
| 5 | 🤷 Graceful failure message | All else fails |

---

## Key Components

### Document Ingestion & Chunking

Reads **PDF, DOCX, and TXT** files from a `./data/` folder. Documents are split into overlapping chunks with sentence-boundary-aware splitting to preserve coherence.

- **Chunk size:** 800 characters
- **Overlap:** 200 characters
- Skips files over 5MB to prevent crashes
- Supports recursive folder scanning

---

### Vector Store (FAISS)

Text chunks are encoded into **384-dimensional vectors** using `paraphrase-multilingual-MiniLM-L12-v2` (a multilingual sentence transformer). FAISS enables fast cosine similarity search at query time.

- Index is **cached to disk** (`vector_store.pkl`) and only rebuilt when source documents change
- Supports 50+ languages including English and Greek

---

### Query Preprocessing & Expansion

User queries are cleaned, abbreviated terms expanded, and up to **4 query variations** are generated before searching.

**Example:**
```
Input:  "how to submit hw"
Expanded: ["how to submit homework assignment",
           "submit homework assignment",
           "steps to submit homework assignment",
           "guide for submit homework assignment"]
```

Abbreviation expansions include: `hw → homework assignment`, `prof → professor instructor`, `pwd → password`, and more.

---

### Hybrid Re-ranking

Retrieved chunks are re-scored using a **combination of**:
- Semantic similarity (FAISS cosine score)
- Keyword matching (BM25-style token overlap)

Top results are then aggregated with adjacent chunks for fuller context. A "Key point" sentence is highlighted at the top of the answer if a highly relevant sentence is found.

---

### FAQ System

Bilingual FAQ files (`knowledge_base_en.py` / `knowledge_base_el.py`) are embedded at startup. User queries are matched against FAQ embeddings via cosine similarity.

- **Confidence threshold:** 60%
- English queries also fall back to the Greek FAQ via the multilingual model
- FAQ answers are prefixed with a ℹ️ note when served from the cross-lingual fallback

---

### AI Generative Fallback

When documents and FAQs fail to answer, the system invokes a **local generative model** via HuggingFace's `pipeline("text-generation")`:

| File | Model |
|------|-------|
| `TINYLLAMARAG.py` | `TinyLlama/TinyLlama-1.1B-Chat-v1.0` |
| `QWENRAG.py` | Qwen (equivalent pipeline, different model string) |

Both use:
- `bfloat16` precision for memory efficiency
- `device_map="auto"` for GPU/CPU auto-detection
- A structured `<|system|> / <|user|> / <|assistant|>` chat prompt
- Responses capped at **80 new tokens**

---

### Language Detection & Safety

**Language support:**
- Detects **English**, **Greek**, and **Greeklish** (Greek written in Latin characters)
- Uses `langdetect` plus a hand-crafted pattern list of ~30 Greeklish word patterns (e.g., `pws`, `kanw`, `mporo`)
- Unsupported languages (Arabic, Chinese, French, etc.) are blocked with a polite message in the user's preferred language

**Safety filtering (`harmful_content_filter` module):**
- Screens for profanity, harmful content patterns, and dangerous keyword combinations
- Handles **leetspeak** (`h4ck → hack`) and **obfuscated input** (HTML/URL encoded strings like `b&#111;mb`)
- **Gibberish detection** rejects low-vowel-ratio text, keyboard-mash patterns, and excessively repetitive inputs

---

### Response Caching

An in-memory **MD5-keyed cache** avoids re-running the full pipeline for repeated queries.

- Max size: **100 entries**
- TTL: **1 hour**
- Keys are normalized (lowercase + stripped) and include the response language

---

### Flask Web Interface

| Route | Method | Description |
|-------|--------|-------------|
| `/` | `GET` | Renders chat UI with document/chunk count stats |
| `/chat` | `POST` | Accepts JSON `{message, language}`, returns JSON `{response}` |

Language auto-detection runs inside `/chat` — the user's UI language preference is used only as a fallback for block/error messages.

---

## Configuration Reference

| Parameter | Value |
|-----------|-------|
| Chunk size | 800 chars |
| Chunk overlap | 200 chars |
| Min chunk length | 100 chars |
| Top-K retrieval (initial) | 5 |
| Top-K after re-ranking | 3 |
| Document confidence threshold | 45% |
| FAQ confidence threshold | 60% |
| Cache max size | 100 entries |
| Cache TTL | 1 hour |
| Embedding model | `paraphrase-multilingual-MiniLM-L12-v2` |
| Embedding dimensions | 384 |

---

## How to Run

```bash
# 1. Install dependencies (once)
pip install flask sentence-transformers numpy scikit-learn
pip install torch faiss-cpu pypdf python-docx transformers

# 2. Add your documents
# Place PDF, DOCX, or TXT files in the ./data/ folder

# 3. Run
python TINYLLAMARAG.py   # or QWENRAG.py

# 4. Open in browser
# http://localhost:5000
```

---

## Dependencies

| Library | Purpose |
|---------|---------|
| `flask` | Web framework & chat API |
| `sentence-transformers` | Multilingual text embeddings |
| `faiss-cpu` | Fast vector similarity search |
| `transformers` + `torch` | Local AI fallback model |
| `pypdf` | PDF text extraction |
| `python-docx` | Word document extraction |
| `scikit-learn` | Cosine similarity computation |
| `langdetect` | Language identification |
| `numpy` | Vector math |
