##Copyright (c) 2025 Alexandros Panagiotakopoulos
#All Rights Reserved
#DATE: 20/11/2025
#alexandrospanag.github.io

import os
import shutil

def main():
    # Ask user for the file path
    file_path = input("Enter the full path of the file you want to modify:\n> ").strip()

    # Validate file
    if not os.path.isfile(file_path):
        print("Error: File not found. Please check the path and try again.")
        return
    
    # Ask what to replace
    old_word = input("Enter the word/phrase you want to replace:\n> ")
    new_word = input("Enter the replacement word/phrase:\n> ")

    # Create a backup before changing
    backup_path = file_path + ".backup"
    shutil.copy(file_path, backup_path)
    print(f"Backup created at: {backup_path}")

    # Read file contents
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Replace text
    updated_content = content.replace(old_word, new_word)

    # Save modified content
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("\n✔ Replacement complete!")
    print(f"All occurrences of '{old_word}' have been replaced with '{new_word}'.")
    print(f"Updated file saved at: {file_path}")

if __name__ == "__main__":
    main()
