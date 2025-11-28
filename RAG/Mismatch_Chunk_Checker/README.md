# Mismatch Chunk Checker

A comprehensive Python toolkit for managing, expanding, and validating bilingual (English/Greek) FAQ knowledge bases that are chunked for a RAG System. This project includes intelligent RAG-optimized FAQ chunking, content expansion utilities, and synchronization verification tools.

## 📋 Overview

This project provides a complete solution for maintaining high-quality, well-organized knowledge bases that power AI-assisted chatbots and FAQs. The system is specifically designed for the Open eClass LMS platform but can be adapted for any multilingual knowledge base system.

### Key Components

1. **Knowledge Base Files Example**
   - `knowledge_base_en.py` - English FAQ chunks 
   - `knowledge_base_el.py` - Greek FAQ chunks 

2. **Mismatch Chunk Checker** (`Mismatch_Chunk_Checker.py`)
   - Verifies synchronization between English and Greek knowledge bases
   - Identifies missing chunks between versions
   - Generates detailed reports (text and JSON)
   - Provides block-level analysis and statistics

## ✨ Features

### Knowledge Base Organization

- **RAG-Optimized** chunking for improved retrieval accuracy
- **Bilingual Support** with complete English/Greek parity
- **Structured Format** with standardized chunk_id naming

### Coverage Areas

- Authentication & Account Management
- Student Portfolio & Navigation
- Assignments & Submissions with Turnitin Integration
- Attendance Tracking & Management
- Teleconferencing (BigBlueButton, Zoom, Jitsi, Google Meet)
- Communication Tools (Forums, Messages, Chat)
- Assessments & Grading
- Multimedia & Interactive Content
- Calendar & Scheduling
- User Profiles & Settings
- Course Enrollment & Search
- Technical Support
- Advanced Features (Badges, Certificates)
- Wikis & Collaborative Editing
- E-Portfolios & Learning Paths

### Mismatch Checker Features

- ✅ Cross-language chunk verification
- 📊 Detailed statistical analysis
- 📦 Block-level comparison
- 💾 Dual export formats (TXT + JSON)
- 🎯 Synchronization metrics
- 📋 Actionable recommendations


#### Analyzing Knowledge Base

```python
from Mismatch_Chunk_Checker import KnowledgeBaseAnalyzer

# Initialize analyzer
analyzer = KnowledgeBaseAnalyzer(
    en_file='knowledge_base_en.py',
    el_file='knowledge_base_el.py'
)

# Load and analyze
analyzer.load_knowledge_bases()
report = analyzer.generate_report()
print(report)

# Export to files
analyzer.export_report_to_file('report.txt')
analyzer.export_json_report('report.json')
```


### Chunk Categories

- **Authentication** (4 chunks)
- **Course Management** (2 chunks)
- **Communication** (2 chunks)
- **Assignments & Submissions** (2 chunks)
- **Assessments** (2 chunks)
- **Teleconferencing** (8 chunks) - BigBlueButton, Zoom, Jitsi, Google Meet
- **Attendance Tracking** (5 chunks)
- **Rubrics & Grading** (2 chunks)
- **Peer Review** (2 chunks)
- **User Groups** (5 chunks)
- **Student Portfolio** (5 chunks)
- **Advanced Features** (2 chunks)
- **And more...**

## 🔧 Chunk Structure

Each chunk follows a standardized format:

```python
{
    'chunk_id': 'unique_identifier_001',
    'chunk_topic': 'Human-readable topic name',
    'questions': [
        "Question variant 1",
        "Question variant 2",
        "Question variant 3"
    ],
    'answer': """
    Detailed answer content with:
    • Multiple formatting options
    • Clear explanations
    • Step-by-step instructions
    • Important notes
    • Documentation links
    """
}
```

## 📝 Adding New Chunks

### Step 1: Create the Chunk Dictionary

```python
{
    'chunk_id': 'new_feature_001',
    'chunk_topic': 'New Feature Title',
    'questions': [
        "How do I use this?",
        "What does this do?",
        "Feature information"
    ],
    'answer': """
    Your detailed answer here...
    """
}
```

### Step 2: Add to Appropriate Block

```python
CHUNK_NEW_FEATURE = [
    {
        # Your chunk dictionary
    }
]
```

### Step 3: Update Knowledge Base List

```python
KNOWLEDGE_BASE_EN = (
    # ... existing chunks ...
    CHUNK_NEW_FEATURE
)
```

### Step 4: Verify with Mismatch Checker

```bash
python Mismatch_Chunk_Checker.py
```

## 🌐 Bilingual Coverage

Both English and Greek versions maintain:
- Identical chunk_id naming
- Equivalent topic coverage
- Parallel question variations
- Localized answer content
- Consistent formatting and structure

## 📈 Analysis & Reports

The Mismatch Checker generates:

### Text Report (`KB_Mismatch_Report.txt`)
- Overall statistics
- Missing chunks analysis
- Block-level comparison
- Detailed chunk inventory
- Recommendations

### JSON Report (`KB_Mismatch_Report.json`)
```json
{
  "summary": {
    "english_chunks": 68,
    "greek_chunks": 68,
    "synchronization_percentage": 100.0
  },
  "missing_chunks": {
    "in_greek_only": [],
    "in_english_only": []
  },
  "block_analysis": { ... }
}
```

## 🔍 Best Practices

### Content Guidelines

✅ **DO:**
- Use clear, concise language
- Include multiple question variations
- Provide step-by-step instructions
- Add links to official documentation
- Use consistent formatting
- Include examples and use cases

❌ **DON'T:**
- Create overlapping chunks
- Use vague question variations
- Omit important details
- Hardcode file paths
- Mix languages within a chunk

### Maintenance

- Run Mismatch Checker regularly
- Review synchronization reports
- Update outdated information
- Add new features promptly
- Test new chunks before merging

## 🛠️ Technical Details

### Dependencies

- Python 3.7+
- Standard Library only:
  - `re` - Regular expressions
  - `json` - JSON handling
  - `pathlib` - File operations
  - `collections` - Data structures
  - `typing` - Type hints

### File Encoding

All files use **UTF-8 encoding** for proper Greek character support.

### Performance

- Large file handling: ✅ Optimized
- Memory usage: ✅ Minimal
- Processing speed: ✅ <1 second for 68 chunks
- Scalability: ✅ Tested up to 200+ chunks

## 🤝 Contributing

Contributions are welcome! Areas for contribution:

- 📝 Additional FAQ chunks
- 🌍 New language translations
- 🐛 Bug fixes and improvements
- 📊 Enhanced analysis features
- 📚 Documentation improvements
- 🧪 Test cases

### Contribution Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)


## 📄 License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license

### Common Issues

**Q: How do I add a new chunk?**
A: Follow the "Adding New Chunks" section in the documentation.

**Q: Can I use this for other LMS platforms?**
A: Yes! The structure is adaptable. Modify chunk content and topics as needed.

**Q: How often should I run the checker?**
A: Ideally after each modification or weekly for active projects.

**Q: Are there any external dependencies?**
A: No, only Python 3.7+ standard library is required.
---

*Last Updated: November 28, 2025*

**Status**: ✅ Production Ready | **Synchronization**: 100% | **Chunks**: 68/68
