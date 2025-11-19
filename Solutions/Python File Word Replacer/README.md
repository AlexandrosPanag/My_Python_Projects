# 🔄 Text Replacement Utility for Python

A simple yet powerful Python script that performs batch text replacement in any file with automatic backup functionality.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)

## 👤 Author
**Alexandros Panagiotakopoulos**

---

## 📋 Overview

This utility allows you to safely replace all occurrences of a word or phrase in any text-based file. It automatically creates a backup before making changes, ensuring your original file is preserved.

## ✨ Features

- 🔍 **Find & Replace**: Replace all occurrences of any text pattern
- 💾 **Automatic Backup**: Creates a `.backup` copy before modifying
- 🛡️ **Safe Encoding**: Handles UTF-8 files with error tolerance
- ✅ **Validation**: Checks if file exists before processing
- 📝 **User-Friendly**: Simple command-line prompts

---

## 🚀 Usage

### Running the Script

```bash
python text_replacer.py
```

### Interactive Prompts

1. **Enter file path**: Provide the full path to the file you want to modify
2. **Enter search term**: Type the word/phrase you want to replace
3. **Enter replacement**: Type the new word/phrase

### Example Session

```
Enter the full path of the file you want to modify:
> /home/user/documents/story.txt

Enter the word/phrase you want to replace:
> hero

Enter the replacement word/phrase:
> champion

Backup created at: /home/user/documents/story.txt.backup

✔ Replacement complete!
All occurrences of 'hero' have been replaced with 'champion'.
Updated file saved at: /home/user/documents/story.txt
```

---

## 🔧 Technical Details

### Function Reference

| **Function** | **Purpose** |
|--------------|-------------|
| `main()` | Main entry point; handles user interaction and file processing |
| `input().strip()` | Gets user input and removes whitespace |
| `os.path.isfile()` | Validates that the provided path is a valid file |
| `shutil.copy()` | Creates backup copy of the original file |

### File Operations

| **Operation** | **Description** |
|---------------|-----------------|
| `open(file, "r")` | Opens file for reading with UTF-8 encoding |
| `open(file, "w")` | Opens file for writing (overwrites content) |
| `content.replace()` | Performs case-sensitive text replacement |
| `errors="ignore"` | Skips problematic characters during read |

### File Encoding

- **Primary Encoding**: UTF-8
- **Error Handling**: Ignores undecodable characters during read
- **Output**: Always writes in UTF-8

---

## ⚠️ Important Notes

- **Case Sensitive**: The replacement is case-sensitive
- **Backup Location**: Backup file is created in the same directory with `.backup` extension
- **Full File Replacement**: The entire file is read into memory and rewritten
- **No Undo**: Once replaced, use the `.backup` file to restore original content

---

## 💡 Use Cases

- Batch renaming of variables in code files
- Updating terminology across documentation
- Correcting repeated typos in text files
- Refactoring project-wide string references
- Updating configuration file values

---



The script uses the standard Python entry point pattern, ensuring `main()` only runs when executed directly (not when imported as a module).

---

💡 *For questions or contributions, feel free to reach out!*
