# Greek to Greeklish Conversion for RAG Accuracy Testing

A comprehensive testing framework to evaluate whether special Greek characters (diacritics, accents) impact RAG system accuracy. This toolkit converts Greek knowledge bases and test suites to greeklish (Greek using Latin characters) to isolate character encoding as a potential accuracy bottleneck.

## Overview

RAG (Retrieval-Augmented Generation) systems may experience accuracy degradation when processing texts with special Unicode characters, diacritics, and accent marks. This project provides tools to:

1. **Convert knowledge bases** from Greek to Greeklish
2. **Convert test questions** to match knowledge base versions
3. **Run comparative accuracy tests** across multiple configurations
4. **Isolate the impact** of character encoding on RAG performance

## Features

✨ **Complete Greek to Greeklish Mapping**
- All lowercase Greek letters (α-ω)
- All uppercase Greek letters (Α-Ω)
- Accented characters (ά, έ, ή, ί, ό, ύ, ώ)
- Diaeresis marks (ϊ, ϋ)
- Final sigma (ς) handling

🔬 **Four Testing Configurations**
| Configuration | Knowledge Base | Test Questions | Purpose |
|---|---|---|---|
| **Baseline** | Greek | Greek | Current system performance |
| **Full Greeklish** | Greeklish | Greeklish | Test if char encoding is the bottleneck |
| **Mixed 1** | Greek | Greeklish | Isolate query preprocessing issues |
| **Mixed 2** | Greeklish | Greek | Isolate retrieval matching issues |

📊 **Comprehensive Test Suite**
- **BASIC**: 5 direct FAQ matches (easy questions)
- **MEDIUM**: 5 contextual questions requiring inference
- **VAGUE**: 5 ambiguous queries testing robustness
- **HARD**: 5 complex scenarios outside typical FAQ
- **EDGE**: 5 edge cases (gibberish, off-topic, empty input)

⚡ **Performance Metrics**
- Response relevance scoring
- Topic coverage analysis
- Response type classification (RAG, FAQ, AI Generated, Fallback)
- Source citation detection
- Response time measurement

## Files

```
.
├── README.md                              # This documentation
├── greek_to_greeklish_converter.py        # Main converter for knowledge bases
├── convert_test_questions_to_greeklish.py # Converter for test suites
├── knowledge_base_el.py                   # Original Greek knowledge base
├── knowledge_base_greeklish.py            # Converted greeklish knowledge base
├── test_rag_accuracy.py                   # Original Greek test suite
└── test_rag_accuracy_greeklish.py         # Converted greeklish test suite
```

## Installation & Usage

### Quick Start

#### 1. Convert Knowledge Base

```bash
python greek_to_greeklish_converter.py
```

**Output:**
- Analyzes Greek content (character counts, distribution)
- Creates `knowledge_base_greeklish.py`
- Reports conversion statistics

**Example Output:**
```
Greek Content Analysis:
Total characters in file: 149908
Unique Greek characters found: 64
Total Greek character instances: 83258
Percentage of Greek characters: 55.54%

✓ Knowledge base converted successfully!
```

#### 2. Convert Test Questions

```bash
python convert_test_questions_to_greeklish.py
```

**Output:**
- Creates `test_rag_accuracy_greeklish.py`
- Reports Greek characters converted
- Provides testing configuration summary

#### 3. Run Accuracy Tests

**Test Greek vs Greeklish:**
```bash
# In test_rag_accuracy.py or test_rag_accuracy_greeklish.py
# Select option 1 (English), 2 (Greek/Greeklish), or 5 (Both)
python test_rag_accuracy.py
```

## Testing Methodology

### Comparative Testing

This framework enables four distinct test scenarios:

**Scenario 1: Baseline (Greek KB + Greek Questions)**
```bash
python test_rag_accuracy.py
# Select option 2 for Greek questions
# Uses knowledge_base_el.py
```

**Scenario 2: Full Greeklish (Greeklish KB + Greeklish Questions)**
```python
# Modify RAG.py to load knowledge_base_greeklish.py
python test_rag_accuracy_greeklish.py
# Select option 2 for greeklish questions
```

**Scenario 3 & 4: Mixed Configurations**
- Mix Greek KB with Greeklish questions
- Mix Greeklish KB with Greek questions
- Helps identify if issue is in encoding or retrieval

### Interpretation Guide

| Greek Accuracy | Greeklish Accuracy | Interpretation |
|---|---|---|
| **Low** | **High** | ✅ Character encoding IS the issue |
| **Low** | **Low** | ❌ Problem elsewhere (query processing, retrieval logic) |
| **High** | **High** | ❌ Not the bottleneck |
| **High** | **Low** | ⚠️ Greeklish conversion may have degraded data |

## Greek to Greeklish Conversion Examples

| Greek | Greeklish | Notes |
|---|---|---|
| τονικό σύστημα | toniko systima | Basic vowels and consonants |
| Χαιρετισμός | Hairetismos | Accented characters removed |
| Ελληνικά | Ellinika | Final sigma (ς) → s |
| Πώς κάνω; | Pos kano; | Question marks preserved |
| ΨΥΧΟΛΟΓΙΑ | PSUXOLOGIA | Uppercase ψ → PS |

## Performance Considerations

### Conversion Time
- **Knowledge Base**: ~1-2 seconds (149KB file, 83K Greek chars)
- **Test Suite**: <1 second (1400 Greek chars)

### Accuracy Impact
- Test suite includes timing metrics for each response
- Compare `response_time` between configurations
- Greeklish typically processes faster (fewer encoding operations)

## Architecture Details

### Mapping Strategy

The converter uses a comprehensive Unicode mapping for:

**Vowels**: α→a, ε→e, η→i, ο→o, υ→u, ω→o
**Consonants**: β→v, γ→g, δ→d, κ→k, λ→l, μ→m, ν→n, π→p, ρ→r, σ/ς→s, τ→t, φ→f, χ→x, ψ→ps, θ→th, ξ→x, ζ→z

**Accents Removed**:
- Tonos (acute accent): ά, έ, ή, ί, ό, ύ, ώ
- Dialytika (diaeresis): ϊ, ϋ

### Why This Matters

Greek text relies heavily on diacritical marks:
- **55.54%** of knowledge base is Greek characters
- Embeddings may struggle with uncommon Unicode characters
- Tokenizers might split Greek words differently
- Vector similarity could be affected by character encoding

## Known Limitations

1. **Transliteration Quality**: Greeklish is phonetic, not character-perfect
   - No distinction between η/ι (both → i)
   - No distinction between ο/ω (both → o)
   
2. **Context Loss**: Accents contain semantic information in Greek
   - Important for native speakers
   - May affect readability

3. **Proper Nouns**: Names may change meaning or be unrecognizable
   - "Αθήνα" → "Athina" (phonetically correct but different spelling)

## Extending the Framework

### Adding New Question Sets

Edit `test_rag_accuracy.py` or `test_rag_accuracy_greeklish.py`:

```python
NEW_QUESTIONS = [
    {
        "id": "N1",
        "question_en": "Your English question",
        "question_el": "Η ελληνική σας ερώτηση",
        "expected_topics_en": ["topic1", "topic2"],
        "expected_topics_el": ["θέμα1", "θέμα2"],
        "difficulty": "BASIC",
        "notes": "Description"
    }
]
```

### Customizing Character Mappings

Modify `GREEK_TO_GREEKLISH` dictionary in either converter file:

```python
GREEK_TO_GREEKLISH = {
    'χ': 'ch',  # Alternative: x → ch (for χαμόγελο)
    'γ': 'gh',  # Alternative: γ → gh (for γάμος)
}
```

## Requirements

- **Python**: 3.7+
- **Encoding**: UTF-8 (for Greek character support)
- **RAG System**: `RAG.py` with functions:
  - `get_rag_response(question, language)`
  - `preprocess_query(question)`
  - `expand_query(question, language)`

## License

This project is licensed under the **Creative Commons Attribution 4.0 International License (CC-BY-4.0)**.

You are free to:
- ✅ Share and adapt this work
- ✅ Use for commercial purposes
- ✅ Modify and distribute

**Provided that you:**
- ✅ Provide attribution to the original author
- ✅ Include a copy of the license
- ✅ Indicate changes made

For full license details, see: https://creativecommons.org/licenses/by/4.0/

## Author

**Created by**: *[Your Name/Organization]*

**Created**: December 2025

**Purpose**: RAG System Accuracy Testing Framework for Greek Language Processing

## Contributing

This framework was developed to solve a specific RAG accuracy issue with Greek character encoding. If you:
- Discover improvements to the conversion mapping
- Find edge cases in character handling
- Have results from your own testing

Please document findings and share them for the broader community.

## Citation

If you use this framework in research or documentation, please cite:

```
Greek to Greeklish Conversion for RAG Testing (2025)
Author: [Your Name]
License: CC-BY-4.0
URL: [Your Repository/Path]
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'RAG'"
**Solution**: Ensure `RAG.py` is in the same directory as test files.

### Issue: "UnicodeEncodeError" on Windows
**Solution**: Ensure files are saved with UTF-8 encoding. In Python:
```python
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()
```

### Issue: Greeklish results are worse than Greek
**Solution**: This might indicate:
1. Greek embeddings are better trained than English
2. Your RAG system has Greek-specific optimizations
3. The knowledge base quality improved through conversion (data cleaning)

## Related Resources

- **RAG Systems**: https://en.wikipedia.org/wiki/Retrieval-augmented_generation
- **Unicode**: https://unicode.org/reports/tr31/#Identifier_Normalization
- **Greek Language**: https://en.wikipedia.org/wiki/Greek_alphabet
- **Greeklish**: https://en.wikipedia.org/wiki/Greeklish

## FAQ

**Q: Will greeklish affect search for Greek speakers?**
A: Yes, this is a trade-off. This framework is for *testing* whether encoding is your bottleneck, not a production solution. Native Greek is preferred for production systems.

**Q: Can I use this for other languages?**
A: Yes! The mapping structure is language-agnostic. Create new mappings for any language pair.

**Q: How do I integrate this into my RAG pipeline?**
A: Load `knowledge_base_greeklish.py` instead of `knowledge_base_el.py` in your RAG system initialization.

---

**Last Updated**: December 15, 2025

**Status**: ✅ Production Ready for Testing

For questions or issues, refer to the troubleshooting section or consult the framework author.

