# Written by Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# LICENSE: CC-BY-4.0
# Date: 15/12/2025

"""
Convert test questions from Greek to Greeklish
===============================================
Converts all Greek test questions in test_rag_accuracy.py to greeklish
so you can test both versions with matching question sets.
"""

import re

# Comprehensive Greek to Greeklish mapping (same as in converter)
GREEK_TO_GREEKLISH = {
    # Lowercase letters
    'α': 'a',
    'β': 'v',
    'γ': 'g',
    'δ': 'd',
    'ε': 'e',
    'ζ': 'z',
    'η': 'i',
    'θ': 'th',
    'ι': 'i',
    'κ': 'k',
    'λ': 'l',
    'μ': 'm',
    'ν': 'n',
    'ξ': 'x',
    'ο': 'o',
    'π': 'p',
    'ρ': 'r',
    'σ': 's',
    'ς': 's',  # final sigma
    'τ': 't',
    'υ': 'u',
    'φ': 'f',
    'χ': 'x',
    'ψ': 'ps',
    'ω': 'o',
    
    # Uppercase letters
    'Α': 'A',
    'Β': 'V',
    'Γ': 'G',
    'Δ': 'D',
    'Ε': 'E',
    'Ζ': 'Z',
    'Η': 'I',
    'Θ': 'TH',
    'Ι': 'I',
    'Κ': 'K',
    'Λ': 'L',
    'Μ': 'M',
    'Ν': 'N',
    'Ξ': 'X',
    'Ο': 'O',
    'Π': 'P',
    'Ρ': 'R',
    'Σ': 'S',
    'Τ': 'T',
    'Υ': 'U',
    'Φ': 'F',
    'Χ': 'X',
    'Ψ': 'PS',
    'Ω': 'O',
    
    # Accented lowercase letters
    'ά': 'a',
    'έ': 'e',
    'ή': 'i',
    'ί': 'i',
    'ό': 'o',
    'ύ': 'u',
    'ώ': 'o',
    
    # Accented uppercase letters
    'Ά': 'A',
    'Έ': 'E',
    'Ή': 'I',
    'Ί': 'I',
    'Ό': 'O',
    'Ύ': 'U',
    'Ώ': 'O',
    
    # Diaeresis (dialytika)
    'ϊ': 'i',
    'ϋ': 'u',
    'Ϊ': 'I',
    'Ϋ': 'U',
}

def greek_to_greeklish(text):
    """Convert Greek text to Greeklish."""
    result = []
    for char in text:
        if char in GREEK_TO_GREEKLISH:
            result.append(GREEK_TO_GREEKLISH[char])
        else:
            result.append(char)
    return ''.join(result)

def convert_test_file(input_file, output_file):
    """
    Convert test file from Greek to Greeklish.
    
    Args:
        input_file: Path to the original test file
        output_file: Path to save the converted test file
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert all Greek text to Greeklish
    converted_content = greek_to_greeklish(content)
    
    # Save to new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    print(f"✓ Test file converted successfully!")
    print(f"  Original file: {input_file}")
    print(f"  Converted file: {output_file}")
    
    # Count changes
    greek_count = sum(1 for char in content if ord(char) >= 880 and ord(char) <= 1023)
    print(f"  Greek characters converted: {greek_count}")
    
    return True

if __name__ == '__main__':
    input_file = r'c:\Users\username\Desktop\yourpathhere.py'
    output_file = r'c:\Users\username\Desktop\yourpathhere_greeklish.py'
    
    convert_test_file(input_file, output_file)
    
    print(f"\n✓ You can now test both versions:")
    print(f"  - Original (Greek questions): {input_file}")
    print(f"  - Converted (Greeklish questions): {output_file}")
    print(f"\n📝 Now you have matching test suites:")
    print(f"  • Greek KB + Greek questions")
    print(f"  • Greeklish KB + Greeklish questions")
    print(f"  • Or mix and match to isolate variables!")
