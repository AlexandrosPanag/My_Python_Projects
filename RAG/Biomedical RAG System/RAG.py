# By Alexandros Panagiotakopoulos
# Copyright (c) 2025 Alexandros Panagiotakopoulos. All rights reserved.
# Date: 20/06/2025

import os
import re
import json
import sys
import time
import re
import asyncio
import requests
import deep_translator
sys.stdout.reconfigure(encoding='utf-8')

from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import EmbeddingRetriever, PromptNode, PromptTemplate
from haystack.pipelines import Pipeline

from transformers import pipeline as hf_pipeline
from deep_translator import GoogleTranslator


# --------- CONFIGURATION ---------
EN_SRC_FOLDER = r"C:\Users\<fullpath>en\mayoclinic"
EN_JSON_FILE = r"C:\Users\<fullpath>\en\BioASQ-training13b\training13b.json"
EL_SRC_FOLDER_NEW = r"C:\Users\<fullpath>\qtlp_20131010_140423\e4118e7c-c941-4f5c-aca1-b69d81a315f3\xml"
TRANSLATION_OUTPUT_FOLDER = r"C:\Users\<fullpath>\translation_english_to_greek"
WIKI_OUTPUT_FOLDER = r"C:\Users\<fullpath>\assignment_corpus\wikipedia_el_cancer"

EN_TERMS = [
    "hematologic", "blood cancer", "hematological neoplasm", "leukemia",
    "lymphoma", "myeloma", "acute myeloid", "chronic lymphocytic", "CLL",
    "acute lymphoblastic", "chronic myelogenous", "Hodgkin", "nonHodgkin",
    "diffuse large B-cell", "myelodysplastic", "myeloproliferative",
    "monoclonal gammopathy", "Waldenström", "CAR-NK", "CAR-T",
    "stem cell transplant", "minimal residual disease", "hematopoiesis", "bone marrow"
]
GREEK_TERMS = [
    "αιματολογικός καρκίνος", "καρκίνος του αίματος", "λευχαιμία", "λέμφωμα", "μυέλωμα",
    "αιμοποίηση", "μυελός των οστών", "βλαστοκύτταρα", "πλασματοκύτταρα", "Hodgkin",
    "λευκά αιμοσφαίρια", "λεμφικός", "λεμφικά κύτταρα", "λεμφαδένες", "λεμφαδενικός",
    "λεμφαδενίτιδα", "λεμφική κακοήθεια", "λευκοκύτταρα", "αιματολογική κακοήθεια",
    "διαταραχές του μυελού των οστών", "πολλαπλούν μυέλωμα", "νεοπλασία πλασματοκυττάρων",
    "μυελικός καρκίνος", "αιμοποιητικό σύστημα", "αιμοποιητικός ιστός", "μυελικός καρκίνος",
    "αιματολογικές κακοήθειες", "νεοπλασία του αίματος", "οξεία μυελογενής λευχαιμία", "AML",
    "Χρόνια λεμφοκυτταρική λευχαιμία", "CLL", "οξεία λεμφοβλαστική λευχαιμία",
    "χρόνια μυελογενής λευχαιμία", "CML", "διάχυτο μεγαλοκυτταρικό λέμφωμα Β", "DLBCL",
    "μυελοδυσπλαστικά σύνδρομα", "μυελοϋπερπλαστικά νοσήματα", "μονοκλωνική γαμμαπάθεια",
    "μακροσφαιριναιμία Waldenström", "CAR-NK κυτταρική θεραπεία", "CAR-T κυτταρική θεραπεία",
    "μεταμόσχευση αιμοποιητικών βλαστοκυττάρων", "ελάχιστη υπολειπόμενη νόσος",
    "ανοσοθεραπεία", "κυτταρική θεραπεία", "γονιδιακή θεραπεία", "μεταμόσχευση μυελού των οστών",
    "χημειοθεραπεία", "ακτινοθεραπεία", "λεμφαδένες", "λεμφικά αγγεία", "σπλήνας", "θύμος αδένας",
    "μυελός των οστών", "αιμοποιητικός ιστός"
]
GREEK_WIKI_TERMS = [
    "Λευχαιμία", "Λέμφωμα", "Μυέλωμα", "Καρκίνος_του_αίματος", "Αιματολογικός_καρκίνος",
    "Οξεία_μυελογενής_λευχαιμία", "Χρόνια_λεμφοκυτταρική_λευχαιμία", "Χρόνια_μυελογενής_λευχαιμία",
    "Λέμφωμα_Hodgkin", "Λέμφωμα_non-Hodgkin"
]

def contains_terms(text, terms):
    text_lower = text.lower()
    for term in terms:
        if term.lower() in text_lower:
            return True
    return False

# --- REAL TRANSLATION FUNCTION USING HELSINKI-NLP ---
translator = hf_pipeline("translation", model="Helsinki-NLP/opus-mt-en-el")


# THE TRANSLATION TAKES 2 HOURS TO COMPILE, SO FOR FAST COMPILATION, WE CAN USE A MOCK FUNCTION
# Uncomment the following function to use a mock translation for testing purposes.
# Collect all English texts that would be translated
collected_english_texts = []

def translate_to_greek(text):
    # Instead of translating, collect the English text
    collected_english_texts.append(text)
    return "[Greek translation of]: " + text


# SAFE - TRANSLATION FUNCTION
r'''
 def translate_to_greek(text, max_chars=4999, retries=3, delay=10):
    """
    Translates English text to Greek using GoogleTranslator, chunking if needed.
    Handles connection errors and skips empty/oversized chunks.
    Wikipedia fetching is NOT included or called here.

    Args:
        text (str): The English text to translate.
        max_chars (int): Maximum characters per translation chunk (default 4999).
        retries (int): Number of retries for connection errors.
        delay (int): Delay in seconds between retries.

    Returns:
        str: The translated Greek text.
    """
    from deep_translator import GoogleTranslator
    import time
    import re

    def safe_translate(chunk):
        chunk = chunk.strip()
        if not chunk:
            return ""
        # If chunk is still too big, split by characters
        if len(chunk) > max_chars:
            subchunks = [chunk[i:i+max_chars] for i in range(0, len(chunk), max_chars)]
            return "\n".join(safe_translate(sub) for sub in subchunks)
        for attempt in range(retries):
            try:
                return GoogleTranslator(source='en', target='el').translate(chunk)
            except Exception as e:
                if "Text length need to be between 0 and 5000 characters" in str(e):
                    print(f"[Translation error] Chunk length error: {len(chunk)}. Skipping chunk.")
                    return chunk
                print(f"[Translation error] {e}. Retrying {attempt+1}/{retries}...")
                time.sleep(delay)
        print("[Translation error] Failed after retries. Returning original chunk.")
        return chunk

    # First split by sentence, then ensure all chunks are <= max_chars
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= max_chars:
            current += " " + sentence if current else sentence
        else:
            # If current is too big, split it by characters
            if len(current) > max_chars:
                for i in range(0, len(current), max_chars):
                    chunks.append(current[i:i+max_chars].strip())
            elif current.strip():
                chunks.append(current.strip())
            current = sentence
    # Add the last chunk
    if len(current) > max_chars:
        for i in range(0, len(current), max_chars):
            chunks.append(current[i:i+max_chars].strip())
    elif current.strip():
        chunks.append(current.strip())

    # Translate each chunk and join
    greek_text = ""
    for chunk in chunks:
        translated = safe_translate(chunk)
        if translated:
            greek_text += translated + "\n"
        time.sleep(delay)  # Slow down to avoid rate-limiting
    return greek_text.strip()
'''

# EXPIREMENTAL TRANSLATION FUNCTION - WIKIPEDIA VERSION
# Uncomment the following function to use the experimental translation function.
r'''
def translate_to_greek(text, max_chars=5000, retries=3, delay=3):
    """
    Translates English text to Greek using GoogleTranslator, chunking if needed.
    Handles connection errors and skips empty/oversized chunks.
    """
    def safe_translate(chunk):
        chunk = chunk.strip()
        if not chunk:
            return ""
        if len(chunk) > max_chars:
            print(f"[Translation warning] Chunk too long after splitting: {len(chunk)} chars. Splitting further.")
            # Split further by characters
            subchunks = [chunk[i:i+max_chars] for i in range(0, len(chunk), max_chars)]
            return "\n".join(safe_translate(sub) for sub in subchunks)
        for attempt in range(retries):
            try:
                return GoogleTranslator(source='en', target='el').translate(chunk)
            except Exception as e:
                # If the error is about length, don't retry
                if "Text length need to be between 0 and 5000 characters" in str(e):
                    print(f"[Translation error] Chunk length error: {len(chunk)}. Skipping chunk.")
                    return chunk
                print(f"[Translation error] {e}. Retrying {attempt+1}/{retries}...")
                time.sleep(delay)
        print("[Translation error] Failed after retries. Returning original chunk.")
        return chunk

    # Split text into sentences and then into chunks
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= max_chars:
            current += " " + sentence if current else sentence
        else:
            if current.strip():
                chunks.append(current.strip())
            current = sentence
    if current.strip():
        chunks.append(current.strip())
    # Translate each chunk and join
    greek_text = ""
    for chunk in chunks:
        translated = safe_translate(chunk)
        if translated:
            greek_text += translated + "\n"
    return greek_text.strip()
'''


# Filter and translate TXT files
## This function reads TXT files, filters them based on specific terms, and translates them to Greek
def filter_and_translate_txt(): # Filter and translate TXT files
    os.makedirs(TRANSLATION_OUTPUT_FOLDER, exist_ok=True) # Ensure output folder exists
    for filename in os.listdir(EN_SRC_FOLDER): # List all files in the source folder
        if filename.endswith(".txt"): # Process only TXT files
            with open(os.path.join(EN_SRC_FOLDER, filename), "r", encoding="utf-8") as f: # Read the file
                text = f.read() # Read the content of the file
            if contains_terms(text, EN_TERMS): # Check if the text contains any of the English terms
                greek_text = translate_to_greek(text) # Translate the text to Greek
                out_path = os.path.join(TRANSLATION_OUTPUT_FOLDER, filename.replace(".txt", "_el.txt")) # Prepare output path
                with open(out_path, "w", encoding="utf-8") as out_f: # Write the translated text to the output file
                    out_f.write(greek_text) # Save the translated text
                print(f"Saved translated TXT: {out_path}") # Print confirmation of saved file


# Filter and translate JSON files
# This function reads a JSON file, filters questions based on specific terms, translates them to Greek
def filter_and_translate_json(): # Filter and translate JSON files
    if not os.path.exists(EN_JSON_FILE): # Check if the JSON file exists
        print("JSON file not found.") # If not found, print a message and return
        return # Stop processing if JSON file is not found
    with open(EN_JSON_FILE, "r", encoding="utf-8") as f: # Open the JSON file for reading
        data = json.load(f) # Load the JSON data
    for idx, item in enumerate(data.get("questions", [])): # Iterate through each question in the JSON data
        text_fields = [] # Initialize a list to hold text fields
        if "body" in item: # If the question has a body field
            text_fields.append(item["body"]) # Add the body text to the list
        if "ideal_answer" in item and isinstance(item["ideal_answer"], list): # If the question has an ideal answer field and it's a list
            text_fields.extend(item["ideal_answer"]) # Add all ideal answers to the list
        text = "\n".join(text_fields) # Join all text fields into a single string
        if contains_terms(text, EN_TERMS): # Check if the text contains any of the English terms
            greek_text = translate_to_greek(text) # Translate the text to Greek
            out_path = os.path.join(TRANSLATION_OUTPUT_FOLDER, f"bioasq_q{idx+1}_el.txt") # Prepare output path for the translated file
            with open(out_path, "w", encoding="utf-8") as out_f: # Open the output file for writing
                out_f.write(greek_text) # Write the translated text to the output file
            print(f"Saved translated JSON: {out_path}") # Print confirmation of saved file

def filter_and_translate_xml(): # Filter and translate XML files
    if not os.path.exists(EL_SRC_FOLDER_NEW): # Check if the XML source folder exists
        print("XML folder not found.") # If not found, print a message and return
        return # Stop processing if XML folder is not found
    for filename in os.listdir(EL_SRC_FOLDER_NEW): # List all files in the XML source folder
        if filename.endswith(".xml"): # Process only XML files
            file_path = os.path.join(EL_SRC_FOLDER_NEW, filename) # Prepare the full path to the XML file
            with open(file_path, "r", encoding="utf-8") as f: # Open the XML file for reading
                text = f.read() # Read the content of the XML file
            if contains_terms(text, EN_TERMS): # Check if the text contains any of the English terms
                greek_text = translate_to_greek(text) # Translate the text to Greek
                out_path = os.path.join(TRANSLATION_OUTPUT_FOLDER, filename.replace(".xml", "_el.txt")) # Prepare output path for the translated file
                with open(out_path, "w", encoding="utf-8") as out_f: # Open the output file for writing
                    out_f.write(greek_text) # Write the translated text to the output file
                print(f"Saved translated XML: {out_path}") # Print confirmation of saved file

def fetch_wikipedia_intro(term): # Fetch Wikipedia introduction for a given term
    url = "https://el.wikipedia.org/w/api.php" # Wikipedia API URL
    params = {  
        "action": "query", 
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": term,
        "format": "json",
        "redirects": 1
    }
    response = requests.get(url, params=params) # Make a GET request to the Wikipedia API
    data = response.json() # Parse the JSON response
    pages = data.get("query", {}).get("pages", {}) # Get the pages from the response
    for page_id, page in pages.items(): # Iterate through each page
        if "extract" in page and page["extract"]: # If the page has an extract
            return page["extract"] # Return the extract as the introduction
    return None # If no extract is found, return None

def fetch_and_save_wikipedia(): # Fetch and save Wikipedia articles for Greek cancer terms
    os.makedirs(WIKI_OUTPUT_FOLDER, exist_ok=True) # Ensure the output folder exists
    for term in GREEK_WIKI_TERMS: # Iterate through each term in the Greek Wikipedia terms list
        print(f"Fetching Wikipedia for: {term}") # Print the term being fetched
        intro = fetch_wikipedia_intro(term) # Fetch the Wikipedia introduction for the term
        if intro: # If an introduction is found
            filename = os.path.join(WIKI_OUTPUT_FOLDER, f"{term}.txt") # Prepare the filename for saving
            with open(filename, "w", encoding="utf-8") as f: # Open the file for writing
                f.write(intro) # Write the introduction to the file
            print(f"Saved Wikipedia: {filename}") # Print confirmation of saved file
        else: # If no introduction is found
            print(f"No Wikipedia entry found for: {term}") # Print a message indicating no entry was found

def load_biomedical_documents(): # Load biomedical documents from various sources
    docs = [] # Initialize an empty list to hold documents
    # English MayoClinic .txt files
    for filename in os.listdir(EN_SRC_FOLDER): # List all files in the English source folder
        if filename.endswith(".txt"): # Process only TXT files
            with open(os.path.join(EN_SRC_FOLDER, filename), "r", encoding="utf-8") as f: # Open the file for reading
                text = f.read() # Read the content of the file
            if contains_terms(text, EN_TERMS): # Check if the text contains any of the English terms
                docs.append({"content": text, "meta": {"filename": filename, "lang": "en"}}) # Append the document to the list with metadata
    # English BioASQ JSON
    if os.path.exists(EN_JSON_FILE): # Check if the BioASQ JSON file exists
        with open(EN_JSON_FILE, "r", encoding="utf-8") as f: # Open the JSON file for reading
            data = json.load(f) # Load the JSON data
        for idx, item in enumerate(data.get("questions", [])): # Iterate through each question in the JSON data
            text_fields = [] # Initialize a list to hold text fields
            if "body" in item: # If the question has a body field
                text_fields.append(item["body"]) # Add the body text to the list 
            if "ideal_answer" in item and isinstance(item["ideal_answer"], list): # If the question has an ideal answer field and it's a list
                text_fields.extend(item["ideal_answer"]) # If the question has an ideal answer field and it's a list, add all ideal answers to the list
            text = "\n".join(text_fields) # Join all text fields into a single string
            if contains_terms(text, EN_TERMS): # Check if the text contains any of the English terms
                docs.append({"content": text, "meta": {"filename": f"bioasq_q{idx+1}.txt", "lang": "en"}}) # Append the document to the list with metadata
    # Greek XML files
    for filename in os.listdir(EL_SRC_FOLDER_NEW): # List all files in the Greek XML source folder
        if filename.endswith(".xml"): # Process only XML files
            with open(os.path.join(EL_SRC_FOLDER_NEW, filename), "r", encoding="utf-8") as f: # Open the file for reading
                text = f.read() # Read the content of the file
            if contains_terms(text, GREEK_TERMS): # Check if the text contains any of the Greek terms
                docs.append({"content": text, "meta": {"filename": filename, "lang": "el"}}) # Append the document to the list with metadata
    # Wikipedia Greek files
    if os.path.exists(WIKI_OUTPUT_FOLDER): # Check if the Wikipedia output folder exists
        for filename in os.listdir(WIKI_OUTPUT_FOLDER): # List all files in the Wikipedia output folder
            if filename.endswith(".txt"): # Process only TXT files
                with open(os.path.join(WIKI_OUTPUT_FOLDER, filename), "r", encoding="utf-8") as f: # Open the file for reading
                    text = f.read() # Read the content of the file
                docs.append({"content": text, "meta": {"filename": filename, "lang": "el"}}) # Append the document to the list with metadata
    return docs  # Return the list of documents loaded from various sources

def build_haystack_pipeline(): # Build the Haystack RAG pipeline
    document_store = InMemoryDocumentStore(embedding_dim=384) # Initialize an in-memory document store with specified embedding dimension
    docs = load_biomedical_documents() # Load biomedical documents from various sources
    document_store.write_documents(docs) # Write the loaded documents to the document store
    retriever = EmbeddingRetriever( # Initialize the EmbeddingRetriever for the Haystack pipeline
        document_store=document_store, # Use the document store to retrieve documents
        embedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", # Use a multilingual model for embeddings
        use_gpu=True # Use GPU for the retriever
    )
    document_store.update_embeddings(retriever) # Update embeddings for the retriever
    prompt_node = PromptNode( # Initialize the PromptNode for the Haystack pipeline
        model_name_or_path="google/flan-t5-large", # Use the FLAN-T5 model for the prompt node
        default_prompt_template=PromptTemplate("Given the context, answer the question.\nContext: {join(documents)}\nQuestion: {query}\nAnswer:"), # Define the prompt template for the prompt node
        use_gpu=True # Use GPU for the prompt node
    )
    pipe = Pipeline() # Initialize the Haystack pipeline
    pipe.add_node(component=retriever, name="Retriever", inputs=["Query"]) # Add the retriever node to the pipeline
    pipe.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"]) # Add the prompt node to the pipeline
    return pipe 

if __name__ == "__main__":
    print("Filtering and collecting English documents...")  # Start of the filtering and collecting process
    os.makedirs(TRANSLATION_OUTPUT_FOLDER, exist_ok=True)  # Ensure output folder exists
    filter_and_translate_txt()  # Filter and collect TXT files
    filter_and_translate_json()  # Filter and collect JSON files
    filter_and_translate_xml()  # Filter and collect XML files
    print("Done filtering and collecting.\n")  # End of the filtering and collecting process

    # Save all collected English texts into a single file
    output_path = os.path.join(TRANSLATION_OUTPUT_FOLDER, "english_terms_fetched_not_translated.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(collected_english_texts))
    print(f"Saved all English texts to: {output_path}")

    print("Fetching Wikipedia articles for bonus...")  # Start of the Wikipedia fetching process
    fetch_and_save_wikipedia()  # Fetch and save Wikipedia articles related to cancer in Greek
    print("Wikipedia collection complete!\n")  # End of the Wikipedia collection

    print("Building Haystack RAG pipeline and indexing biomedical documents...")  # Start of the pipeline setup
    pipe = build_haystack_pipeline()  # Build the Haystack RAG pipeline
    print("Ready!\n")  # End of the pipeline setup

    test_questions = [
        "Τι είναι η λευχαιμία;",
        "Ποια είναι τα συμπτώματα του λεμφώματος;",
        "Τι είναι το μυέλωμα;",
        "Τι είναι η μεταμόσχευση μυελού των οστών;",
        "Τι είναι η CAR-T θεραπεία;",
        "What is leukemia?",
        "What are the symptoms of lymphoma?",
        "What is myeloma?",
        "What is bone marrow transplantation?",
        "What is CAR-T therapy?",
    ]

    print("=== HAYSTACK RAG SYSTEM TEST ===\n")  # Start of the RAG system test
    for idx, q in enumerate(test_questions, 1):
        print(f"Q{idx}: {q}")
        prediction = pipe.run(
            query=q,
            params={"Retriever": {"top_k": 5}}
        )
        print("Raw prediction:", prediction)
        answers = prediction.get("answers", [])
        if answers and hasattr(answers[0], "answer"):
            print("Answer:", answers[0].answer)
        elif "results" in prediction and prediction["results"]:
            print("Answer:", prediction["results"][0])
        else:
            print("No answer found.")
        print("-----")
    print("\nRAG system test completed.")


def process_greek_translations():
    """
    Reads successful_fetched_translation.txt and saves each Greek translation
    as a separate file for manual or automated review.
    """
    INPUT_FILE = os.path.join(TRANSLATION_OUTPUT_FOLDER, "successful_fetched_translation.txt")
    OUTPUT_FOLDER = os.path.join(TRANSLATION_OUTPUT_FOLDER, "final_greek_texts")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    if not os.path.exists(INPUT_FILE):
        print(f"File not found: {INPUT_FILE}")
        return
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    greek_blocks = [block.strip() for block in content.split("\n\n") if block.strip()]
    for idx, block in enumerate(greek_blocks, 1):
        out_path = os.path.join(OUTPUT_FOLDER, f"greek_translation_{idx}.txt")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(block)
        print(f"Saved Greek translation: {out_path}")
    print("All Greek translations have been saved for review.")

# Add this call at the end of your main block:
if __name__ == "__main__":
    # ...existing main code...
    print("\nProcessing Greek translations from successful_fetched_translation.txt...")
    process_greek_translations()
