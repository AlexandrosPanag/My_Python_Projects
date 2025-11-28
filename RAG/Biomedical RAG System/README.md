# Biomedical RAG System Information Retrieval System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)

## 👤 Author
**Alexandros Panagiotakopoulos**


## Overview

This project implements a **Retrieval-Augmented Generation (RAG) system** for biomedical information extraction and question-answering in both English and Greek. It processes medical documents from multiple sources (Mayo Clinic, BioASQ, Wikipedia) and builds an intelligent document retrieval pipeline using Haystack and transformer models.

---

## Purpose

The system addresses the need for **multilingual biomedical information retrieval**, specifically focusing on hematologic cancers (blood cancers) and related medical treatments. It performs the following core operations:

1. **Document Collection & Filtering** - Collects medical documents related to hematologic cancers
2. **Translation Pipeline** - Translates English medical documents to Greek using transformer models
3. **Wikipedia Enrichment** - Fetches authoritative Greek Wikipedia articles for key medical terms
4. **RAG Pipeline Construction** - Builds an intelligent retrieval-augmented generation system
5. **Multilingual Q&A** - Answers medical questions in both English and Greek

---

## Key Features

### 1. **Multi-Source Document Ingestion**
- **Mayo Clinic TXT files** - Clinical documentation from Mayo Clinic (English)
- **BioASQ JSON** - Biomedical question-answering dataset (English)
- **Medical XML files** - Greek medical texts (QTLP Medical EL corpus)
- **Wikipedia Integration** - Greek Wikipedia articles on cancer topics

### 2. **Intelligent Document Filtering**
Filters documents based on domain-specific terminology:
- **English terms:** Leukemia, lymphoma, myeloma, CAR-T therapy, stem cell transplant, etc. (48 terms)
- **Greek terms:** Λευχαιμία, λέμφωμα, μυέλωμα, and related medical terminology (48+ terms)

### 3. **Translation Pipeline**
- Uses Helsinki-NLP OPUS MT model (`Helsinki-NLP/opus-mt-en-el`) for neural machine translation
- Implements chunk-based translation with automatic error handling
- Supports GoogleTranslator as fallback with retry logic
- Processes large documents by splitting into sentence-level chunks (max 5000 characters)

### 4. **Haystack RAG System**
- **Document Store:** InMemoryDocumentStore for fast retrieval
- **Embeddings:** Multilingual embeddings via `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- **Retriever:** EmbeddingRetriever with semantic search capabilities
- **Generator:** FLAN-T5 Large model for natural language generation
- **GPU Support:** Optional GPU acceleration for embeddings and generation

### 5. **Multilingual Q&A**
Supports both Greek and English medical questions:
- *Ελληνικά:* "Τι είναι η λευχαιμία;", "Ποια είναι τα συμπτώματα του λεμφώματος;"
- *English:* "What is leukemia?", "What are the symptoms of lymphoma?"

---

## Architecture

### Component Structure

```
MTP333_Biomedical_Assignment.py
├── Configuration Section
│   ├── Folder paths (EN, EL, output folders)
│   ├── Terminology lists (EN_TERMS, GREEK_TERMS, GREEK_WIKI_TERMS)
│   └── Model initialization (Helsinki-NLP translator)
│
├── Utility Functions
│   ├── contains_terms() - Filter documents by medical terminology
│   └── fetch_wikipedia_intro() - Fetch Wikipedia articles
│
├── Document Processing Pipeline
│   ├── filter_and_translate_txt() - Process English TXT files
│   ├── filter_and_translate_json() - Process BioASQ JSON
│   ├── filter_and_translate_xml() - Process Greek medical XML
│   ├── fetch_and_save_wikipedia() - Fetch Wikipedia articles
│   └── process_greek_translations() - Save Greek translations
│
├── RAG System
│   ├── load_biomedical_documents() - Load all filtered documents
│   ├── build_haystack_pipeline() - Create RAG pipeline
│   └── Pipeline components:
│       ├── Retriever (semantic search)
│       ├── PromptNode (FLAN-T5 generation)
│       └── Query pipeline
│
└── Main Execution
    ├── Collect and filter documents
    ├── Translate to Greek
    ├── Fetch Wikipedia articles
    ├── Build RAG pipeline
    └── Test with 10 medical questions (5 Greek + 5 English)
```

### Data Flow

```
Input Documents
    ↓
┌───────────────────────────┐
│ Document Filtering        │
│ (by medical terms)        │
└───────────────────────────┘
    ↓
┌───────────────────────────┐
│ Translation (EN→EL)       │
│ (Helsinki-NLP / Google)   │
└───────────────────────────┘
    ↓
┌───────────────────────────┐
│ Wikipedia Enrichment      │
│ (fetch Greek articles)    │
└───────────────────────────┘
    ↓
┌───────────────────────────┐
│ Document Indexing         │
│ (compute embeddings)      │
└───────────────────────────┘
    ↓
┌───────────────────────────┐
│ Haystack RAG Pipeline     │
├───────────────────────────┤
│ Query Input (EN/EL)       │
│ ↓                         │
│ Retriever (top-5)         │
│ ↓                         │
│ FLAN-T5 Generator         │
│ ↓                         │
│ Answer Output             │
└───────────────────────────┘
```

---

## Installation & Setup

### Requirements

- **Python 3.7+**
- **Deep Learning Models:** Requires downloading ~2-3 GB of models
- **GPU:** Recommended (NVIDIA CUDA-compatible GPU for faster processing)

### Dependencies

```bash
pip install torch transformers haystack deep-translator requests
```

### Specific Package Versions

```
torch>=1.9.0           # PyTorch framework
transformers>=4.10.0   # Hugging Face transformers
haystack>=1.0          # Haystack RAG framework
deep-translator>=1.8   # Translation support
requests>=2.26         # HTTP requests for Wikipedia
```

### Configuration

Update the following paths in the script to match your system:

```python
EN_SRC_FOLDER = r"C:\Users\[username]\Desktop\assignment_corpus\en\mayoclinic"
EN_JSON_FILE = r"C:\Users\[username]\Desktop\assignment_corpus\en\BioASQ-training13b\training13b.json"
EL_SRC_FOLDER_NEW = r"C:\Users\[username]\Desktop\assignment_corpus\el\QTLP_MED_EL_nonCC\..."
TRANSLATION_OUTPUT_FOLDER = r"C:\Users\[username]\Desktop\assignment_corpus\translation_english_to_greek"
WIKI_OUTPUT_FOLDER = r"C:\Users\[username]\Desktop\assignment_corpus\wikipedia_el_cancer"
```

---

## Usage

### Basic Execution

```bash
python MTP333_Biomedical_Assignment.py
```

### Step-by-Step Execution

The script performs the following operations when run:

#### 1. **Document Collection & Filtering**
```python
# Filters and collects English TXT, JSON, and XML files based on medical terminology
filter_and_translate_txt()      # Mayo Clinic TXT files
filter_and_translate_json()     # BioASQ JSON questions
filter_and_translate_xml()      # Greek medical XML documents
```
**Output:** `english_terms_fetched_not_translated.txt` - All relevant English texts

#### 2. **Wikipedia Article Fetching**
```python
fetch_and_save_wikipedia()
```
**Output:** Individual `.txt` files for each Wikipedia article in `wikipedia_el_cancer/` folder

#### 3. **RAG Pipeline Construction**
```python
pipe = build_haystack_pipeline()
```
- Loads all filtered documents
- Computes multilingual embeddings
- Creates retriever + FLAN-T5 generator pipeline

#### 4. **Test Q&A System**
The script runs 10 test questions (5 Greek + 5 English):

```python
test_questions = [
    "Τι είναι η λευχαιμία;",                           # What is leukemia?
    "Ποια είναι τα συμπτώματα του λεμφώματος;",       # What are symptoms of lymphoma?
    "Τι είναι το μυέλωμα;",                            # What is myeloma?
    "Τι είναι η μεταμόσχευση μυελού των οστών;",      # What is bone marrow transplant?
    "Τι είναι η CAR-T θεραπεία;",                      # What is CAR-T therapy?
    "What is leukemia?",
    "What are the symptoms of lymphoma?",
    "What is myeloma?",
    "What is bone marrow transplantation?",
    "What is CAR-T therapy?",
]
```

**Example Output:**
```
Q1: Τι είναι η λευχαιμία;
Answer: Leukemia is a type of blood cancer characterized by abnormal white blood cell production...
-----
```

---

## Medical Terminology Coverage

### English Terms (48)
Hematologic cancers, blood cancer, hematological neoplasm, leukemia, lymphoma, myeloma, acute myeloid, chronic lymphocytic, CLL, acute lymphoblastic, chronic myelogenous, Hodgkin, nonHodgkin, diffuse large B-cell, myelodysplastic, myeloproliferative, monoclonal gammopathy, Waldenström, CAR-NK, CAR-T, stem cell transplant, minimal residual disease, hematopoiesis, bone marrow

### Greek Terms (48+)
Αιματολογικός καρκίνος, καρκίνος του αίματος, λευχαιμία, λέμφωμα, μυέλωμα, αιμοποίηση, μυελός των οστών, βλαστοκύτταρα, πλασματοκύτταρα, και πολλά άλλα

### Wikipedia Topics (10)
- Λευχαιμία (Leukemia)
- Λέμφωμα (Lymphoma)
- Μυέλωμα (Myeloma)
- Καρκίνος του αίματος (Blood Cancer)
- Αιματολογικός καρκίνος (Hematologic Cancer)
- Λέμφωμα Hodgkin (Hodgkin Lymphoma)
- Λέμφωμα non-Hodgkin (Non-Hodgkin Lymphoma)
- And more...

---

## Core Functions Explained

### Document Processing

#### `filter_and_translate_txt()`
Processes Mayo Clinic English text files:
1. Reads each `.txt` file from `EN_SRC_FOLDER`
2. Checks if content contains medical terms (using `contains_terms()`)
3. Translates relevant documents to Greek
4. Saves as `filename_el.txt` in output folder

#### `filter_and_translate_json()`
Processes BioASQ biomedical questions:
1. Loads JSON containing biomedical Q&A pairs
2. Extracts question body and ideal answers
3. Filters by medical terminology
4. Translates and saves as `bioasq_q{n}_el.txt`

#### `filter_and_translate_xml()`
Processes Greek medical XML documents:
1. Reads XML files from QTLP Medical EL corpus
2. Filters by medical terminology
3. Translates (if needed) and saves output

#### `fetch_and_save_wikipedia()`
Fetches Greek Wikipedia articles:
1. For each term in `GREEK_WIKI_TERMS`
2. Calls Wikipedia API: `https://el.wikipedia.org/w/api.php`
3. Extracts introductory text
4. Saves as `{term}.txt` for reference

### RAG Pipeline

#### `load_biomedical_documents()`
Aggregates all processed documents:
1. Loads filtered English TXT files
2. Loads BioASQ JSON questions
3. Loads Greek XML files
4. Loads Wikipedia articles
5. Returns list of document dictionaries with metadata

**Document Format:**
```python
{
    "content": "Medical text content...",
    "meta": {
        "filename": "source_file.txt",
        "lang": "en" or "el"  # Language code
    }
}
```

#### `build_haystack_pipeline()`
Constructs the RAG system:

```python
# 1. Create document store
document_store = InMemoryDocumentStore(embedding_dim=384)

# 2. Load and index documents
docs = load_biomedical_documents()
document_store.write_documents(docs)

# 3. Initialize retriever (multilingual embeddings)
retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    use_gpu=True
)
document_store.update_embeddings(retriever)

# 4. Initialize generator (FLAN-T5)
prompt_node = PromptNode(
    model_name_or_path="google/flan-t5-large",
    default_prompt_template=PromptTemplate(
        "Given the context, answer the question.\n"
        "Context: {join(documents)}\n"
        "Question: {query}\n"
        "Answer:"
    ),
    use_gpu=True
)

# 5. Create pipeline
pipe = Pipeline()
pipe.add_node(component=retriever, name="Retriever", inputs=["Query"])
pipe.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"])
```

---

## Translation Options

The script provides **three translation approaches**:

### Option 1: Mock Translation (Fastest - Default)
```python
def translate_to_greek(text):
    collected_english_texts.append(text)
    return "[Greek translation of]: " + text
```
- **Speed:** Instant
- **Use Case:** Testing, development
- **Limitation:** No actual translation

### Option 2: Google Translator (Production)
Located in commented `r'''...'''` block - safe production version with:
- Retry logic (configurable attempts)
- Chunk-based splitting (max 5000 chars)
- Error handling for oversized chunks
- Rate-limiting delay between requests

### Option 3: Wikipedia-Enhanced Translation
Alternative implementation with Wikipedia integration - supports full pipeline with external knowledge enrichment.

To use production translation, uncomment the relevant function:
```python
def translate_to_greek(text, max_chars=4999, retries=3, delay=10):
    # ... production translation code ...
```

---

## Output Structure

### File Organization

```
assignment_corpus/
├── en/
│   ├── mayoclinic/              # Source English TXT files
│   └── BioASQ-training13b/      # Source BioASQ JSON
├── el/
│   └── QTLP_MED_EL_nonCC/       # Source Greek XML files
├── translation_english_to_greek/
│   ├── *.txt                     # Translated English→Greek documents
│   ├── english_terms_fetched_not_translated.txt  # All collected English texts
│   └── final_greek_texts/        # Processed Greek translations (optional)
└── wikipedia_el_cancer/
    ├── Λευχαιμία.txt            # Wikipedia articles (individual files)
    ├── Λέμφωμα.txt
    └── ...
```

### Report Files

- `english_terms_fetched_not_translated.txt` - Consolidated English source texts
- `KB_Mismatch_Report.txt` - (If validation tool used)
- `KB_Mismatch_Report.json` - (If validation tool used)

---

## Models & Transformers Used

| Component | Model | Purpose | Size |
|-----------|-------|---------|------|
| **Translator** | Helsinki-NLP/opus-mt-en-el | English→Greek translation | ~150 MB |
| **Embeddings** | paraphrase-multilingual-MiniLM-L12-v2 | Multilingual semantic embeddings | ~384 MB |
| **Generator** | google/flan-t5-large | Answer generation from context | ~770 MB |
| **Tokenizer** | T5 tokenizer | Tokenization for FLAN-T5 | ~1 MB |

**Total Model Size:** ~1.3 GB (downloaded on first use)

---

## Performance Considerations

### Processing Time Estimates

- **Document Filtering:** 1-2 minutes (depends on corpus size)
- **Translation:** 2+ hours (English→Greek for large corpus)
- **Wikipedia Fetching:** 2-5 minutes (10 articles, includes API delays)
- **Haystack Indexing:** 10-30 minutes (depends on document count and GPU)
- **Q&A Testing:** 30 seconds - 2 minutes (10 questions, depends on document retrieval size)

### GPU Requirements

- **Recommended:** NVIDIA GPU with 4+ GB VRAM
- **Minimum:** 2 GB VRAM
- **Fallback:** CPU mode (significantly slower, ~5-10x slower)

### Memory Usage

- **Document Store:** ~100-500 MB (depends on corpus)
- **Embeddings:** ~200-800 MB (depends on number of documents)
- **Models:** ~2-3 GB (loaded in memory)
- **Total:** 3-5 GB RAM recommended

---

## Troubleshooting

### Common Issues

#### 1. **Translation Timeout**
```
Error: Connection timeout during translation
```
**Solution:**
- Increase `delay` parameter in `translate_to_greek()`
- Use mock translation for testing
- Check internet connection
- Try GoogleTranslator fallback

#### 2. **Out of Memory**
```
Error: CUDA out of memory or Insufficient memory
```
**Solution:**
- Reduce document batch size
- Use CPU mode (disable GPU)
- Process documents in smaller chunks
- Reduce embedding dimension

#### 3. **Wikipedia API Error**
```
Error: No Wikipedia entry found for term
```
**Solution:**
- Check term spelling (must match Wikipedia)
- Use English term with Greek translation
- Skip missing terms (script continues automatically)

#### 4. **Model Download Failure**
```
Error: Failed to download model from Hugging Face
```
**Solution:**
- Check internet connection
- Verify Hugging Face is accessible in your region
- Pre-download models manually:
  ```bash
  python -c "from transformers import pipeline; pipeline('translation', model='Helsinki-NLP/opus-mt-en-el')"
  ```

#### 5. **Encoding Issues with Greek Text**
```
Error: UnicodeDecodeError: 'utf-8' codec can't decode...
```
**Solution:**
- Ensure UTF-8 encoding: Already configured via `sys.stdout.reconfigure(encoding='utf-8')`
- Check file encoding when saving outputs
- Use `encoding='utf-8'` when opening files

---

## Extension Ideas

### Future Enhancements

1. **Additional Language Support**
   - Spanish (es), French (fr), German (de) translations
   - Use `Helsinki-NLP/opus-mt-en-{lang}` models

2. **Advanced NLP Features**
   - Named Entity Recognition (NER) for medical entities
   - Medical relationship extraction
   - Biomedical ontology integration (SNOMED CT, UMLS)

3. **Enhanced Retrieval**
   - Semantic similarity reranking
   - Hybrid retrieval (BM25 + semantic)
   - Query expansion techniques

4. **User Interface**
   - Web interface (Flask/Streamlit)
   - Chat-based Q&A interface
   - Document upload & indexing UI

5. **Evaluation Metrics**
   - BLEU scores for translation quality
   - Retrieval metrics (MRR, nDCG)
   - Answer quality assessment

6. **Persistent Storage**
   - Replace InMemoryDocumentStore with Elasticsearch/PostgreSQL
   - Build searchable document index
   - Cache computed embeddings

---

## References

### Datasets Used
- **Mayo Clinic:** Clinical documentation corpus
- **BioASQ:** Biomedical semantic question-answering dataset (http://bioasq.org)
- **QTLP Medical EL:** Greek medical text corpus (nonCC version)
- **Greek Wikipedia:** Medical articles (https://el.wikipedia.org)

### Libraries & Frameworks
- **Haystack:** End-to-end QA framework (https://github.com/deepset-ai/haystack)
- **Transformers:** Hugging Face transformer models (https://huggingface.co)
- **Deep Translator:** Translation wrapper library (https://github.com/nidhaloff/deep-translator)
- **Sentence Transformers:** Multilingual embeddings (https://www.sbert.net)

### Pre-trained Models
- Helsinki-NLP OPUS MT: Neural machine translation
- FLAN-T5: Instruction-following text generation
- Multilingual MiniLM: Cross-lingual semantic embeddings

---


## 📄 License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license
---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-06-20 | Initial release - Full RAG system with EN/EL support |
| TBD | TBD | GPU optimization, additional languages |

---

## Appendix: Quick Reference

### Running a Single Query
```python
# After RAG pipeline is built
result = pipe.run(
    query="Τι είναι η λευχαιμία;",
    params={"Retriever": {"top_k": 5}}
)
print(result["answers"][0].answer if result["answers"] else "No answer found")
```

### Batch Processing Multiple Questions
```python
questions = [
    "Τι είναι η λευχαιμία;",
    "What is leukemia?",
    "Ποια είναι τα συμπτώματα;"
]

for q in questions:
    result = pipe.run(query=q, params={"Retriever": {"top_k": 5}})
    print(f"Q: {q}")
    print(f"A: {result['answers'][0].answer if result['answers'] else 'N/A'}\n")
```

### Adding Custom Documents
```python
# Add new documents to the system
new_docs = [
    {"content": "Your medical text...", "meta": {"filename": "custom.txt", "lang": "en"}}
]
document_store.write_documents(new_docs)
document_store.update_embeddings(retriever)
```

