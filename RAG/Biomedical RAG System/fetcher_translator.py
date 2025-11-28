# By Alexandros Panagiotakopoulos
# Copyright (c) 2025 Alexandros Panagiotakopoulos. All rights reserved.
# Date: 20/06/2025

from deep_translator import GoogleTranslator
import time

INPUT_FILE = "C:/Users/alexa/Desktop/assignment_corpus/translation_english_to_greek/english_terms_fetched_not_translated.txt"
OUTPUT_FILE = "C:/Users/alexa/Desktop/assignment_corpus/translation_english_to_greek/successful_fetched_translation.txt"

def split_text(text, max_chars=5000):
    # Split by paragraphs, then by sentences, then by chars if needed
    import re
    blocks = []
    for paragraph in text.split("\n\n"):
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)
        current = ""
        for sentence in sentences:
            if len(current) + len(sentence) + 1 <= max_chars:
                current += " " + sentence if current else sentence
            else:
                if current:
                    blocks.append(current.strip())
                current = sentence
        if current:
            blocks.append(current.strip())
    # If any block is still too big, split by chars
    final_blocks = []
    for block in blocks:
        if len(block) > max_chars:
            for i in range(0, len(block), max_chars):
                final_blocks.append(block[i:i+max_chars])
        else:
            final_blocks.append(block)
    return final_blocks

def translate_block(text, retries=3, delay=3):
    translations = []
    for chunk in split_text(text):
        for attempt in range(retries):
            try:
                return GoogleTranslator(source='en', target='el').translate(chunk)
            except Exception as e:
                if "Text length need to be between 0 and 5000 characters" in str(e):
                    print(f"[Translation error] Chunk too long: {len(chunk)}. Skipping chunk.")
                    return chunk
                print(f"[Translation error] {e}. Retrying {attempt+1}/{retries}...")
                time.sleep(delay)
        print("[Translation error] Failed after retries. Returning original text.")
        return chunk

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    english_blocks = [block.strip() for block in content.split("\n\n") if block.strip()]
    translations = []
    for idx, block in enumerate(english_blocks, 1):
        print(f"Translating block {idx}/{len(english_blocks)}...")
        translation = translate_block(block)
        translations.append(translation)
        time.sleep(2)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(translations))
    print(f"All translations saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
