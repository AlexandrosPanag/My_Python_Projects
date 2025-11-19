##Copyright (c) 2025 Alexandros Panagiotakopoulos
#All Rights Reserved
#DATE: 20/11/2025
#alexandrospanag.github.io

import os
import shutil

def main():
    # ============================================
    # CONFIGURATION SECTION - EDIT THESE VALUES
    # ============================================
    
    # Set the full path to your file here
    file_path = r"C:\Users\YourName\Documents\example.txt"
    
    # Set what you want to replace
    old_word = "old_text"
    
    # Set the replacement text
    new_word = "new_text"
    
    # ============================================
    # SCRIPT EXECUTION - DO NOT EDIT BELOW
    # ============================================
    
    print("=" * 60)
    print("🔄 TEXT REPLACEMENT UTILITY - PATH FILE VERSION")
    print("=" * 60)
    print()
    
    # Display configuration
    print("📋 Current Configuration:")
    print(f"   File Path: {file_path}")
    print(f"   Search For: '{old_word}'")
    print(f"   Replace With: '{new_word}'")
    print()
    
    # Validate file
    if not os.path.isfile(file_path):
        print("❌ Error: File not found!")
        print(f"   The file '{file_path}' does not exist.")
        print("   Please edit the 'file_path' variable in the script.")
        input("\nPress Enter to exit...")
        return
    
    # Confirm before proceeding
    print("⚠️  WARNING: This will modify the file!")
    confirm = input("Do you want to proceed? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("\n🚫 Operation cancelled by user.")
        input("Press Enter to exit...")
        return
    
    print()
    
    # Create a backup before changing
    backup_path = file_path + ".backup"
    try:
        shutil.copy(file_path, backup_path)
        print(f"✅ Backup created at: {backup_path}")
    except Exception as e:
        print(f"❌ Error creating backup: {e}")
        input("\nPress Enter to exit...")
        return
    
    # Read file contents
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        input("\nPress Enter to exit...")
        return
    
    # Count occurrences
    occurrence_count = content.count(old_word)
    
    if occurrence_count == 0:
        print(f"\n⚠️  No occurrences of '{old_word}' found in the file.")
        print("   No changes were made.")
        input("\nPress Enter to exit...")
        return
    
    # Replace text
    updated_content = content.replace(old_word, new_word)
    
    # Save modified content
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
    except Exception as e:
        print(f"❌ Error writing to file: {e}")
        print("   Your original file is safe in the backup.")
        input("\nPress Enter to exit...")
        return
    
    print()
    print("=" * 60)
    print("✔️  REPLACEMENT COMPLETE!")
    print("=" * 60)
    print(f"📊 Replaced {occurrence_count} occurrence(s) of '{old_word}'")
    print(f"📝 Updated file: {file_path}")
    print(f"💾 Backup saved: {backup_path}")
    print()
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
