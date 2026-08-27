#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ RAG.py ║
# ║ Retrieval-Augmented Generation Chatbot System ║
#
╠══════════════════════════════════════════════════════════════════════════════╣
# ║ Code written by: Alexandros Panagiotakopoulos ║
# ║ Institution: Hellenic Mediterranean University (HMU) ║
# ║ Department: Informatics Engineering ║
# ║ Project: MASTER'S THESIS ║
# ║ Academic ID: MTP333 ║
# ║ Semester: Winter 2025-2026 ║
# ║ Copyright (c) 2025-2026 Alexandros Panagiotakopoulos ║
# ║ License: CC BY-NC-SA 4.0 ║
# ║ https://creativecommons.org/licenses/by-nc-sa/4.0/ ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
#
#
┌──────────────────────────────────────────────────────────────────────────────┐
# │ HOW TO RUN THIS PROGRAM │
#
├──────────────────────────────────────────────────────────────────────────────┤
# │ 1. Open Command Prompt/Terminal │
# │ 2. Navigate to this folder: │
# │ CD C:\Users\alexa\Desktop │
# │ 3. Install required packages (only once): │
# │ pip install flask sentence-transformers numpy scikit-learn │
# │ pip install torch faiss-cpu pypdf python-docx transformers │
# │ 4. Run the program: │
# │ python RAG.py │
# │ 5. Open browser and go to: http://localhost:5000 │
#
└──────────────────────────────────────────────────────────────────────────────┘
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║ TRUE RAG SYSTEM - Enhanced LMS Chatbot for Open eClass ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ ║
║ WHAT IS RAG? (Retrieval-Augmented Generation) ║
║ ───────────────────────────────────────────── ║
║ RAG is an AI technique that combines: ║
║ • RETRIEVAL: Finding relevant documents from a knowledge base ║
║ • GENERATION: Creating human-like responses based on those documents ║
║ ║
║ Think of it like a smart librarian who: ║
║ 1. Understands your question (even if you phrase it differently) ║
║ 2. Finds the right books/pages that contain the answer ║
║ 3. Summarizes the information for you ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ HOW THIS SYSTEM WORKS (Step by Step): ║
║ ───────────────────────────────────── ║
║ ║
║ STARTUP PHASE (happens once when program starts): ║
║ 1. DOCUMENT INGESTION: Reads all PDF, DOCX, TXT files from 'data'
folder ║
║ 2. CHUNKING: Splits documents into smaller overlapping pieces ║
║ 3. VECTORIZATION: Converts text pieces into numerical representations
║
║ 4. INDEXING: Stores these numbers in FAISS for fast searching ║
║ ║
║ QUERY PHASE (happens every time user asks a question): ║
║ 1. PREPROCESSING: Cleans and expands the user's question ║
║ 2. RETRIEVAL: Finds most similar document pieces using vector math ║
║ 3. RE-RANKING: Double-checks results using keyword matching ║
║ 4. RESPONSE: Returns the best answer with source citations ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ FALLBACK HIERARCHY (if one method fails, try the next): ║
║ ───────────────────────────────────────────────────── ║
║ Primary: Search through document corpus (RAG) ║
║ Secondary: Match against predefined FAQ database ║
║ Tertiary: Use TinyLlama AI to generate an answer ║
║ Final: Suggest user rephrases or provides documentation link ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ FEATURES: ║
║ ───────── ║
║ ✓ Bilingual support (English & Greek) ║
║ ✓ Document ingestion (PDF, DOCX, TXT) ║
║ ✓ Semantic search with FAISS vector indexing ║
║ ✓ Query expansion for better matching ║
║ ✓ Hybrid re-ranking (semantic + keyword) ║
║ ✓ FAQ fallback with cross-lingual support ║
║ ✓ Local AI fallback (TinyLlama - runs offline) ║
║ ✓ Safety filter for inappropriate queries ║
║ ✓ Web-based chat interface ║
║ ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ LIBRARY IMPORTS ║
# ║ These are external tools/libraries that provide functionality we
need ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# --- WEB FRAMEWORK ---
# Flask: A lightweight web framework that lets us create a website/API
# - Flask: The main application class
# - render_template: Loads HTML files to display to users
# - request: Access data sent by users (like their chat messages)
# - jsonify: Convert Python data to JSON format for web responses
from flask import Flask, render_template, request, jsonify
# --- MATHEMATICAL & DATA PROCESSING ---
# random: Generate random numbers (used for various purposes)
import random
# numpy (np): Powerful math library for working with arrays of numbers
# Essential for vector operations in semantic search
import numpy as np
# pickle: Read/write binary data files (used for saving/loading data)
import pickle
# harmful_content_filter: Custom module containing harmful content
patterns
from harmful_content_filter import (
HARMFUL_PATTERNS,
PROFANITY_WORDS,
LEETSPEAK_MAP,
BLOCK_MESSAGES,
decode_obfuscated_input
)
# version_checker: Module to check Open eClass documentation updates
try:
from version_checker import check_version_and_warn
except ImportError:
print("Warning: version_checker module not found. Skipping version
checks.")
def check_version_and_warn():
return {'online_version': 'UNKNOWN', 'local_version': '4.2',
'is_outdated': False, 'is_online': False}
# urllib.parse: For URL encoding user queries
import urllib.parse
# --- AI & MACHINE LEARNING ---
# SentenceTransformer: Converts text into numerical vectors
(embeddings)
# This is the "brain" that understands the meaning of text
from sentence_transformers import SentenceTransformer
# cosine_similarity: Measures how similar two vectors are
# Returns a value from -1 (opposite) to 1 (identical)
# We use this to find text with similar meaning to user questions
from sklearn.metrics.pairwise import cosine_similarity
# --- FILE SYSTEM & UTILITIES ---
# os: Interact with the operating system (create folders, check files,
etc.)
import os
# re: Regular expressions for text pattern matching and manipulation
import re
# json: Handle JSON data format (reading/writing structured data)
import json
# Path: Modern way to work with file paths across different operating
systems
from pathlib import Path
# typing: Provides type hints for better code documentation
# - List: A collection of items [item1, item2, item3]
# - Dict: A dictionary with key-value pairs {key: value}
# - Tuple: An immutable pair/group of values (value1, value2)
from typing import List, Dict, Tuple
# --- VECTOR DATABASE ---
# FAISS (Facebook AI Similarity Search): Ultra-fast similarity search
# Can search through millions of vectors in milliseconds
# This is what makes our chatbot respond quickly
import faiss
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ OPTIONAL DOCUMENT PROCESSING ║
# ║ These libraries read different file formats. They're optional
because ║
# ║ the system can still work without them (just won't read those file
types) ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# --- PDF READING ---
# pypdf: Modern library for reading PDF files
# We use try/except because the user might not have it installed
try:
from pypdf import PdfReader # Reads PDF files page by page
except ImportError:
PdfReader = None # Set to None so we can check if it's available later
# --- WORD DOCUMENT READING ---
# python-docx: Library for reading Microsoft Word (.docx) files
try:
from docx import Document # Reads Word documents paragraph by paragraph
except ImportError:
Document = None # Set to None so we can check if it's available later
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ ENHANCED SAFETY CHECKER FOR RAG.py ║
# ║ Replace the old is_safe_query() and is_gibberish() functions with
this ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ LANGUAGE DETECTION & VALIDATION ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
try:
from langdetect import detect, LangDetectException
LANGDETECT_AVAILABLE = True
except ImportError:
print("⚠️ langdetect not installed. Install with: pip install
langdetect")
LANGDETECT_AVAILABLE = False
def is_greeklish(text: str) -> bool:
"""
Detect if text is Greeklish (Greek written with Latin characters).
Examples:
"kalimera" → True (good morning)
"ti kaneis" → True (how are you)
"pws mporo na" → True (how can I)
"""
# ═══ ENGLISH WHITELIST - Skip greeklish check for common English ═══
# These phrases were being incorrectly flagged as greeklish
english_indicators = [
'how do i', 'what is', 'how does', 'where is', 'when is',
'can i', 'tell me', 'help me', 'i want', 'i need',
'doesn\'t work', 'does not work', 'it work', 'how it',
'my grades', 'my course', 'my assignment', 'my password',
'the forum', 'the button', 'the video', 'the calendar',
'submit', 'upload', 'download', 'login', 'logout', 'log in',
'log out',
'feedback', 'assignment', 'enrolled', 'course', 'student',
'sso', 'single sign', 'gdpr', 'security', 'configure',
'joke', 'weather', 'hello', 'thank you', 'please'
]
text_lower = text.lower()
# If any English indicator is found, it's NOT greeklish
for indicator in english_indicators:
if indicator in text_lower:
return False
# Common Greeklish patterns
greeklish_patterns = [
r'\b(pws\|pos)\b', # πώς/πως (how)
r'\b(tha\|8a)\b', # θα (will)
r'\b(den\|dhn)\b', # δεν (not)
r'\b(gia\|ya)\b', # για (for)
r'\b(stin\|sthn)\b', # στην (in the)
r'\b(mou\|mu)\b', # μου (my)
r'\b(sou\|su)\b', # σου (your)
r'\b(kane\|kanw\|kano)\b', # κάνω (do)
r'\b(mporo\|boro)\b', # μπορώ (can)
r'\b(exw\|echo\|exo)\b', # έχω (have)
r'\b(eiste\|iste)\b', # είστε (are)
r'\b(einai\|ine)\b', # είναι (is)
r'\b(kala\|kali)\b', # καλά/καλή (good)
r'\b(kalimera)\b', # καλημέρα (good morning)
r'\b(efxaristo\|efharisto)\b', # ευχαριστώ (thank you)
r'\b(parakalo\|parakalw)\b', # παρακαλώ (please)
r'\b(nai\|ne)\b', # ναι (yes)
r'\b(oxi\|ohi\|ochi)\b', # όχι (no)
r'\b(mathima\|ma8ima)\b', # μάθημα (course)
r'\b(ergasia)\b', # εργασία (assignment)
r'\b(syndesi\|syndesh)\b', # σύνδεση (login)
r'\b(logarjasmo\|logarjazmo)\b', # λογαριασμό (account)
r'\b(fotiti\|fotitis)\b', # φοιτητή/φοιτητής (student)
r'\b(dimioyrgo\|dhmiourgo)\b', # δημιουργώ (create)
r'\b(ypovalo\|ypobalo\|ypobal)\b', # υποβάλλω (submit)
r'\b(vro\|vre\|vrisko)\b', # βρω/βρε/βρίσκω (find)
r'\b(mathimata\|ma8imata)\b', # μαθήματα (courses)
r'\b(eggrafome\|eggrafmai)\b', # εγγράφομαι (enroll)
r'\b(pou)\b', # πού (where)
r'\b(ti)\b', # τι (what)
r'\b(afto\|auto)\b', # αυτό (this)
r'\b(prepei)\b', # πρέπει (must)
r'\b(meta)\b', # μετά (after)
r'\b(kati)\b', # κάτι (something)
r'\b(provlima\|problima)\b', # πρόβλημα (problem)
r'\b(doulevei\|douleuei)\b', # δουλεύει (works)
r'\b(allakso\|allaxo)\b', # αλλάξω (change)
r'\b(yparchei)\b', # υπάρχει (exists)
]
# Check for greeklish patterns
matches = sum(1 for pattern in greeklish_patterns if re.search(pattern,
text_lower))
# If 1+ greeklish words found, it's likely greeklish (lowered from 2)
if matches >= 1:
return True
# REMOVED: Consonant cluster check was too aggressive
# It was flagging English words like "feedback", "strength", etc.
return False
def detect_language(text: str) -> str:
"""
Detect if text is English, Greek, Greeklish, or unsupported language.
Returns:
'en' - English
'el' - Greek
'greeklish' - Greek with Latin characters
'unsupported' - Other language (Arabic, Chinese, etc.)
"""
# ═══ ENGLISH PHRASE WHITELIST ═══
# Check for common English phrases FIRST (before any other detection)
english_phrases = [
'how do i', 'what is', 'how does', 'where is', 'when is',
'why is',
'can i', 'tell me', 'help me', 'i want', 'i need', 'i
forgot',
'doesn\'t work', 'does not work', 'it work', 'how it', 'does
it',
'my grades', 'my course', 'my assignment', 'my password', 'my
account',
'view my', 'see my', 'check my', 'change my', 'update my',
'the forum', 'the button', 'the video', 'the calendar', 'the
course',
'submit', 'upload', 'download', 'login', 'logout', 'log in',
'log out',
'feedback', 'assignment', 'enrolled', 'course', 'student',
'professor',
'sso', 'single sign', 'gdpr', 'security', 'configure',
'settings',
'joke', 'weather', 'hello', 'thank you', 'please', 'help',
'it doesn', 'doesn\'t', 'can\'t', 'won\'t', 'isn\'t',
]
text_lower = text.lower().strip()
# Check for Greek characters FIRST
has_greek_chars = bool(re.search(r'[α-ωΑ-ΩάέήίόύώΆΈΉΊΌΎΏ]', text))
if has_greek_chars:
return 'el'
# Check for Greeklish patterns BEFORE English whitelist
# This allows mixed queries like "Borite na eksigisete...
synchronous"
if is_greeklish(text):
return 'greeklish'
# THEN check English phrases (for pure English queries)
for phrase in english_phrases:
if phrase in text_lower:
return 'en'
# Use langdetect if available (only for non-Greeklish text)
if LANGDETECT_AVAILABLE:
try:
# Only run detection on longer text (more reliable)
if len(text.strip()) < 15:
# Short text - default to English (too ambiguous for detection)
return 'en'
detected = detect(text)
# Accept only English and Greek
if detected in ['en', 'el']:
return detected
# For other detected languages, check if they're "close" to English
# (might be English with typos/shorthand)
close_to_english = ['da', 'nl', 'no', 'sv', 'de', 'fr',
'es', 'it', 'pt', 'ro', 'ca', 'cy', 'af']
if detected in close_to_english:
# Likely English or European language - allow it
return 'en'
# Reject clearly different languages (Arabic, Chinese, etc.)
return 'unsupported'
except LangDetectException:
# Detection failed - default to English for short/ambiguous text
return 'en'
# Fallback: assume English if no Greek detected
return 'en'
def get_language_block_message(language: str = 'en') -> str:
"""
Get appropriate block message for unsupported languages.
Args:
language: User's preferred UI language ('en' or 'el')
Returns:
Block message string in the appropriate language
"""
messages = {
'en': "⚠️ Sorry, I only support **English** and **Greek**
languages.\n\nPlease ask your question in:\n• English\n• Greek
(Ελληνικά)\n• Greeklish (Greek with Latin characters)",
'el': "⚠️ Λυπάμαι, υποστηρίζω μόνο **Αγγλικά** και
**Ελληνικά**.\n\nΠαρακαλώ κάντε την ερώτησή σας σε:\n• Αγγλικά
(English)\n• Ελληνικά\n• Greeklish (Ελληνικά με λατινικούς
χαρακτήρες)"
}
return messages.get(language, messages['en'])
def normalize_leetspeak(text: str) -> str:
"""
Convert leetspeak to normal text for better detection.
Examples:
'h4ck' → 'hack'
'b0mb' → 'bomb'
'sh!t' → 'shit'
"""
normalized = text.lower()
for leet, normal in LEETSPEAK_MAP.items():
normalized = normalized.replace(leet, normal)
return normalized
def remove_obfuscation(text: str) -> str:
"""
Remove common obfuscation techniques.
Examples:
'b o m b' → 'bomb'
'b-o-m-b' → 'bomb'
'b_o_m_b' → 'bomb'
'b.o.m.b' → 'bomb'
"""
# Remove spaces between single characters
text = text.replace(' ', '')
# Remove common separators
for sep in ['-', '_', '.', '*', '+']:
text = text.replace(sep, '')
return text.lower()
def check_harmful_content(query: str, language: str = 'en') -> Dict:
"""
Check if query contains harmful content or profanity.
NOW WITH HTML/URL DECODING!
Returns:
{
'is_safe': bool,
'category': str,
'severity': str,
'block_message': str
}
"""
# ═══ DECODE OBFUSCATED INPUT FIRST ═══
# This catches attempts like "b&#111;mb" or "b%6Fmb"
query = decode_obfuscated_input(query)
print(f"[SAFETY] Decoded query: {query}") # For debugging
query_lower = query.lower().strip()
query_normalized = normalize_leetspeak(query_lower)
query_clean = remove_obfuscation(query_lower)
# Combine all variations for checking
query_variants = [query_lower, query_normalized, query_clean]
# ═══ CHECK 1: HARMFUL CONTENT PATTERNS ═══
for category, patterns in HARMFUL_PATTERNS.items():
# Check both languages
all_patterns = patterns.get('en', []) + patterns.get('el', [])
for pattern in all_patterns:
# Check all query variants
for variant in query_variants:
if pattern in variant:
print(f"[SAFETY BLOCK] Category: {category}, Pattern:
'{pattern}'")
return {
'is_safe': False,
'category': category,
'severity': 'high',
'block_message': BLOCK_MESSAGES.get(category,
BLOCK_MESSAGES['default']).get(language,
BLOCK_MESSAGES['default']['en'])
}
# ═══ CHECK 2: PROFANITY ═══
profanity_found = []
# Split query into words for word-level checking
words = query_lower.split()
words_normalized = query_normalized.split()
# Check both languages
all_profanity = PROFANITY_WORDS.get('en', []) +
PROFANITY_WORDS.get('el', [])
for profane_word in all_profanity:
# Check if profanity appears as whole word or in longer words
for word_list in [words, words_normalized]:
for word in word_list:
# Exact match
if word == profane_word:
profanity_found.append(profane_word)
# Part of longer word (but not in common words)
elif profane_word in word and len(profane_word) > 3:
# Avoid false positives (e.g., 'assess' contains 'ass')
if not any(safe in word for safe in ['class', 'pass', 'mass',
'glass', 'grass']):
profanity_found.append(profane_word)
# Remove duplicates
profanity_found = list(set(profanity_found))
if profanity_found:
print(f"[PROFANITY DETECTED] Words: {profanity_found}")
return {
'is_safe': False,
'category': 'profanity',
'severity': 'medium',
'block_message': BLOCK_MESSAGES['profanity'].get(language,
BLOCK_MESSAGES['profanity']['en'])
}
# ═══ CHECK 3: CONTEXTUAL HARMFUL COMBINATIONS ═══
# Check for dangerous combinations of otherwise innocent words
dangerous_combos = [
['how', 'make', 'explosive'],
['how', 'build', 'weapon'],
['how', 'create', 'virus'],
['steps', 'hack'],
['tutorial', 'bypass'],
['guide', 'crack'],
['πως', 'φτιάξω', 'βόμβα'],
['πως', 'σκοτώσω'],
]
for combo in dangerous_combos:
if all(word in query_lower for word in combo):
print(f"[SAFETY BLOCK] Dangerous combination: {combo}")
return {
'is_safe': False,
'category': 'violence',
'severity': 'high',
'block_message': BLOCK_MESSAGES['violence'].get(language,
BLOCK_MESSAGES['violence']['en'])
}
# ═══ ALL CHECKS PASSED ═══
return {
'is_safe': True,
'category': None,
'severity': None,
'block_message': None
}
def is_gibberish(query: str) -> bool:
"""
Enhanced gibberish detection.
Detects:
- Random character sequences
- Keyboard mashing
- Excessive repetition
- Invalid character ratios
"""
# Remove spaces and convert to lowercase
clean_query = query.lower().replace(' ', '')
# Ignore very short queries (< 5 chars)
if len(clean_query) < 5:
return False
# ═══ CHECK 1: VOWEL RATIO ═══
vowels = set('aeiouαεηιοωυάέήίόύώ') # English + Greek vowels with
accents
vowel_count = sum(1 for c in clean_query if c in vowels)
vowel_ratio = vowel_count / len(clean_query) if len(clean_query) > 0
else 0
# Too few vowels = likely gibberish
if vowel_ratio < 0.15:
print(f"[GIBBERISH] Low vowel ratio: {vowel_ratio:.2%}")
return True
# ═══ CHECK 2: REPEATED CHARACTERS ═══
import itertools
max_repeat = max((len(list(g)) for k, g in
itertools.groupby(clean_query)), default=0)
if max_repeat > 4:
print(f"[GIBBERISH] Excessive repetition: {max_repeat} chars")
return True
# ═══ CHECK 3: KEYBOARD PATTERNS ═══
# Common keyboard mashing patterns
keyboard_patterns = [
'asdf', 'qwer', 'zxcv', 'hjkl', 'uiop',
'asdfg', 'qwerty', 'zxcvb', 'mnbv', 'poiuy',
'jkl;', 'lkjh', 'fdsa', 'rewq'
]
for pattern in keyboard_patterns:
if pattern in clean_query:
print(f"[GIBBERISH] Keyboard pattern detected: {pattern}")
return True
# ═══ CHECK 4: EXCESSIVE CONSONANTS ═══
consonants = set('bcdfghjklmnpqrstvwxyzβγδζθκλμνξπρσςτφχψ')
consonant_clusters = 0
for i in range(len(clean_query) - 3):
if all(c in consonants for c in clean_query[i:i+4]):
consonant_clusters += 1
cluster_ratio = consonant_clusters / max(len(clean_query) - 3, 1)
if cluster_ratio > 0.4:
print(f"[GIBBERISH] High consonant cluster ratio:
{cluster_ratio:.2%}")
return True
# ═══ CHECK 5: VALID CHARACTERS ═══
# Check if query contains mostly valid text characters
valid_chars = set('abcdefghijklmnopqrstuvwxyzαβγδεζηθικλμνξοπρστυφχψω
'
'άέήίόύώ0123456789.,!?\'"-()[]{}:;')
invalid_count = sum(1 for c in query.lower() if c not in valid_chars)
invalid_ratio = invalid_count / len(query) if len(query) > 0 else 0
if invalid_ratio > 0.3:
print(f"[GIBBERISH] High invalid character ratio:
{invalid_ratio:.2%}")
return True
# ═══ CHECK 6: VERY LONG WORDS ═══
words = query.split()
if any(len(word) > 25 for word in words):
print(f"[GIBBERISH] Excessively long word detected")
return True
return False
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ REQUEST CACHING (REPETITION PREVENTION) ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# Simple in-memory cache for recent queries
# Structure: {query_hash: {'response': str, 'timestamp': float,
'language': str}}
QUERY_CACHE = {}
CACHE_MAX_SIZE = 100 # Maximum number of cached queries
CACHE_EXPIRY_SECONDS = 3600 # Cache expires after 1 hour (3600 seconds)
import hashlib # For generating unique hashes
import time # For timestamping cache entries
def get_query_hash(query: str, language: str) -> str:
"""Generate a hash for a query to use as cache key."""
# Normalize query: lowercase, strip whitespace
normalized = query.lower().strip()
# Create hash from query + language
hash_input = f"{normalized}\|{language}" # Combine query and language
return hashlib.md5(hash_input.encode()).hexdigest() # MD5 hash of the
input
def get_cached_response(query: str, language: str) -> str:
"""Check if we have a cached response for this query."""
query_hash = get_query_hash(query, language) # Generate cache key
if query_hash in QUERY_CACHE:
cached = QUERY_CACHE[query_hash] # Retrieve cached entry
# Check if cache is still valid (not expired)
if time.time() - cached['timestamp'] < CACHE_EXPIRY_SECONDS: #
Valid cache
print(f"[CACHE HIT] Returning cached response")
return cached['response']
else:
# Cache expired - remove it
print(f"[CACHE EXPIRED] Removing stale cache entry")
del QUERY_CACHE[query_hash] # Delete expired entry
return None
def cache_response(query: str, language: str, response: str):
"""Store a response in the cache."""
query_hash = get_query_hash(query, language)
# If cache is full, remove oldest entry
if len(QUERY_CACHE) >= CACHE_MAX_SIZE:
# Find oldest entry
oldest_key = min(QUERY_CACHE.keys(),
key=lambda k: QUERY_CACHE[k]['timestamp'])
del QUERY_CACHE[oldest_key]
print(f"[CACHE FULL] Removed oldest entry")
# Store new response
QUERY_CACHE[query_hash] = {
'response': response,
'timestamp': time.time(),
'language': language
}
print(f"[CACHE STORED] Cached response for future requests")
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ FLASK APP INITIALIZATION ║
# ║ Create the web application that will serve our chatbot interface ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# __name__ tells Flask where to find templates and static files
# This creates our web application instance
app = Flask(__name__)
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ QUERY PREPROCESSING & EXPANSION ║
# ║ ║
# ║ PURPOSE: Improve search accuracy by cleaning and expanding user
queries ║
# ║ ║
# ║ WHY THIS MATTERS: ║
# ║ Users often use abbreviations, typos, or different words for the
same ║
# ║ concept. These functions help the system understand what they
really mean. ║
# ║ ║
# ║ EXAMPLE: ║
# ║ User types: "how do i submit hw?" ║
# ║ After preprocessing: "how do i submit hw homework assignment" ║
# ║ This helps match documents about "assignments" even though user
said "hw" ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
def preprocess_query(query: str) -> str:
"""
Clean and normalize user query for better matching.
WHAT THIS FUNCTION DOES:
1. Removes extra spaces (multiple spaces become one)
2. Expands common abbreviations used in education
PARAMETERS:
query (str): The original text the user typed
RETURNS:
str: A cleaned and expanded version of the query
EXAMPLE:
Input: "how do i check my hw"
Output: "how do i check my hw homework assignment"
"""
# STEP 1: Remove extra whitespace
# "hello world" becomes "hello world"
# split() breaks text into words, ' '.join() puts them back with
single spaces
query = ' '.join(query.split())
# STEP 2: Define common abbreviations and their expansions
# These are terms students commonly abbreviate when asking questions
expansions = {
"hw": "homework assignment", # hw -> homework assignment
"prof": "professor instructor", # prof -> professor instructor
"docs": "documents files", # docs -> documents files
"msg": "message", # msg -> message
"msgs": "messages", # msgs -> messages
"pwd": "password", # pwd -> password
"acc": "account", # acc -> account
"enroll": "enrollment register", # enroll -> enrollment register
}
# STEP 3: Check if any abbreviations are in the query and expand them
query_lower = query.lower() # Convert to lowercase for matching
for abbr, expansion in expansions.items():
# Check if the abbreviation is a complete word in the query
if abbr in query_lower.split():
# Add the expansion to the end (keeps original + adds expanded form)
query = query + " " + expansion
# STEP 4: Return the cleaned query (remove any leading/trailing spaces)
return query.strip()
def expand_query(query: str, language: str = 'en') -> List[str]:
"""
Generate query variations for better retrieval coverage.
WHY QUERY EXPANSION?
────────────────────
Sometimes users phrase questions differently than how the answer is
written.
By creating variations of the query, we increase chances of finding
matches.
EXAMPLE:
User asks: "how to submit assignment"
Variations created:
1. "how to submit assignment" (original)
2. "submit assignment" (simplified)
3. "steps to submit assignment" (reformulated)
4. "guide for submit assignment" (reformulated)
PARAMETERS:
query (str): The user's original question
language (str): 'en' for English, 'el' for Greek
RETURNS:
List[str]: A list of query variations (max 4 for speed)
"""
# Start with the original query
variations = [query]
# Convert to lowercase for pattern matching
query_lower = query.lower().strip()
# ─── ENGLISH QUERY EXPANSION ───
if language == 'en':
# Pattern: "how to X" → also search for "X", "steps to X",
"guide for X"
if query_lower.startswith('how to '):
base = query[7:] # Remove "how to " prefix
variations.extend([base, f"steps to {base}", f"guide for {base}"])
# Pattern: "what is X" → also search for "X definition", "X
explanation"
elif query_lower.startswith('what is '):
base = query[8:] # Remove "what is " prefix
variations.extend([base, f"{base} definition", f"{base}
explanation", f"about {base}"])
# Pattern: "where can I find X" → also search for just "X"
elif 'where' in query_lower and 'find' in query_lower:
# Remove the "where can I find" part to get the core topic
variations.append(query.replace('where can I find',
'').replace('where do I find', '').strip())
# ─── GREEK QUERY EXPANSION ───
elif language == 'el':
# Pattern: "πώς X" (how to X) → also search for variations
if query_lower.startswith('πώς '):
base = query[4:] # Remove "πώς " prefix
variations.extend([base, f"βήματα για {base}", f"οδηγίες {base}"])
# Pattern: "τι είναι X" (what is X) → also search for definitions
elif query_lower.startswith('τι είναι '):
base = query[9:] # Remove "τι είναι " prefix
variations.extend([base, f"ορισμός {base}", f"περιγραφή {base}"])
# Return maximum 4 variations to keep searches fast
return variations[:4]
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ CONFIGURATION SETTINGS ║
# ║ ║
# ║ These variables control how the RAG system behaves. ║
# ║ You can adjust these values to tune the system's performance. ║
# ║ ║
# ║ TUNING GUIDE: ║
# ║ • Higher thresholds = More strict (fewer but more accurate results)
║
# ║ • Lower thresholds = More lenient (more results but may be less
relevant) ║
# ║ • Larger chunks = More context but less precise matching ║
# ║ • Smaller chunks = More precise but might miss context ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# ─── DOCUMENT STORAGE ───
# Folder where you put your PDF, Word, and text files
# The system will read all supported files from this folder
DATA_FOLDER = "data"
# ─── CHUNKING PARAMETERS ───
# Documents are split into smaller pieces called "chunks" for better
searching
# Maximum characters per chunk (800 = roughly 100-150 words)
# Larger chunks = more context, but slower and less precise matching
CHUNK_SIZE = 800
# How many characters overlap between consecutive chunks
# This prevents important information from being cut off at chunk
boundaries
# Example: If chunk 1 ends with "To submit an assignment" and chunk 2
starts fresh,
# we might miss the connection. Overlap ensures continuity.
CHUNK_OVERLAP = 200
# ─── RETRIEVAL PARAMETERS ───
# How many results to retrieve and how to filter them
# Number of chunks to retrieve initially (before re-ranking)
# More chunks = better chance of finding the right answer, but slower
TOP_K_CHUNKS = 5
# Number of chunks to return after re-ranking
# This is the final number of sources shown to the user
TOP_K_FINAL = 3
# ─── CONFIDENCE THRESHOLDS ───
# Minimum similarity scores required to consider a match valid
# Scores range from 0 (completely different) to 1 (identical)
# Minimum score for document chunks to be considered relevant
# 0.45 means "at least 45% similar to the query"
DOCUMENT_CONFIDENCE_THRESHOLD = 0.45
# Minimum score for FAQ matches
# 0.60 means "at least 60% similar" - higher because FAQs need more
precision
FAQ_CONFIDENCE_THRESHOLD = 0.60
# ─── ACCURACY ENHANCEMENT SETTINGS ───
# These features improve accuracy but may slightly slow down responses
# Query Expansion: Generate multiple versions of the user's question
# Example: "how to submit" → ["how to submit", "submit", "steps
to submit"]
USE_QUERY_EXPANSION = True
# Re-ranking: After finding results, re-score them using keyword
matching
# Combines semantic similarity (meaning) with keyword matching (exact
words)
USE_RERANKING = True
# Minimum length for a valid text chunk (filters out very short chunks)
MIN_CHUNK_LENGTH = 100
# ─── CREATE DATA FOLDER ───
# Automatically create the data folder if it doesn't exist
# exist_ok=True means "don't error if it already exists"
os.makedirs(DATA_FOLDER, exist_ok=True)
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ SEMANTIC MODEL INITIALIZATION ║
# ║ ║
# ║ This loads the AI model that converts text into numbers
(embeddings) ║
# ║ ║
# ║ HOW SEMANTIC SEARCH WORKS: ║
# ║ 1. Text → Numbers: "How do I submit homework?" → [0.12, -0.45,
0.78, ...] ║
# ║ 2. Similar meanings = Similar numbers ║
# ║ 3. We can compare these numbers to find related content ║
# ║ ║
# ║ MODEL DETAILS: ║
# ║ • Name: paraphrase-multilingual-MiniLM-L12-v2 ║
# ║ • Supports: 50+ languages including English and Greek ║
# ║ • Output: 384-dimensional vectors (384 numbers per text) ║
# ║ • Speed: Fast enough for real-time chat ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# Print a message so user knows the system is loading
print("\n" + "="*70)
print("🚀 RAG SYSTEM STARTUP")
print("="*70)
print("[1/4] Loading semantic model...")
# Load the pre-trained multilingual model from HuggingFace
# First time: Downloads the model (~120MB)
# After that: Loads from local cache (fast)
semantic_model =
SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
# Confirm the model loaded successfully
print(" ✓ Model loaded successfully!")
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ CHECK OPEN eCLASS DOCUMENTATION UPDATES ║
# ║ This runs at startup to alert users if their knowledge base is
outdated ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
print("[2/4] Checking documentation version...")
# Run version check (this will display warnings if documentation is
updated)
version_check_result = check_version_and_warn()
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ OPTIONAL AI LANGUAGE MODEL (TinyLlama) ║
# ║ ║
# ║ This is a LOCAL AI model that can generate human-like responses ║
# ║ when no relevant documents are found in your knowledge base. ║
# ║ ║
# ║ BENEFITS: ║
# ║ • Runs 100% locally - no internet needed after download ║
# ║ • No API keys or subscriptions required ║
# ║ • Free and open source ║
# ║ • Fast inference (works on CPU and GPU) ║
# ║ ║
# ║ WHEN IT'S USED: ║
# ║ • Only when your documents don't contain an answer ║
# ║ • Provides general knowledge responses ║
# ║ • Marked clearly with ⚠️ warning when used ║
# ║ ║
# ║ MODEL: TinyLlama (1.1 billion parameters) ║
# ║ • Small enough to run on regular computers ║
# ║ • Large enough to give decent answers ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# Flag to track if AI fallback is available
# Set to True initially, will be set to False if loading fails
USE_AI_FALLBACK = True
# Placeholder variables for the AI model
# These will be set during loading
ai_model = None # The AI model itself (not used directly with pipeline)
ai_tokenizer = None # The tokenizer (not used directly with pipeline)
# Try to load the AI model - wrapped in try/except because it's
optional
try:
# Import the transformers library for AI models
from transformers import pipeline # High-level API for easy model usage
import torch # PyTorch - the deep learning framework
# Show loading message
print("Loading TinyLlama model (fast, lightweight AI)...")
# Create a text generation pipeline
# This bundles the model + tokenizer + generation logic together
ai_pipeline = pipeline(
"text-generation", # Task: generate text
model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", # Model name on
HuggingFace
dtype=torch.bfloat16, # Use bfloat16 for memory efficiency
device_map="auto", # Auto-detect GPU/CPU
)
# Loading succeeded!
USE_AI_FALLBACK = True
print("✅ TinyLlama loaded successfully! AI-powered answers enabled.")
except ImportError:
# transformers or torch library not installed
print("⚠️ transformers or torch not installed. Running without AI
fallback.")
USE_AI_FALLBACK = False
except Exception as e:
# Some other error (model download failed, GPU error, etc.)
print(f"⚠️ Could not load AI model: {e}")
print(" Running without AI fallback.")
USE_AI_FALLBACK = False
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ DOCUMENT INGESTION & CHUNKING ║
# ║ ║
# ║ This section handles: ║
# ║ 1. Reading documents from various formats (PDF, Word, Text) ║
# ║ 2. Splitting documents into smaller "chunks" for searching ║
# ║ ║
# ║ WHY CHUNKING IS NEEDED: ║
# ║
┌─────────────────────────────────────────────────────────────────────┐
║
# ║ │ Original Document (10,000 words) │ ║
# ║ │
─────────────────────────────────────────────────────────────────│ ║
# ║ │ Chapter 1: Introduction to the University... │ ║
# ║ │ Chapter 2: Academic Policies and Procedures... │ ║
# ║ │ Chapter 3: Student Services and Support... │ ║
# ║ │ ...etc │ ║
# ║
└─────────────────────────────────────────────────────────────────────┘
║
# ║ ↓ ║
# ║ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ║
# ║ │ Chunk 1 │ │ Chunk 2 │ │ Chunk 3 │ │ Chunk 4 │ ... ║
# ║ │ ~150 words│ │ ~150 words│ │ ~150 words│ │ ~150 words│ ║
# ║ └────────────┘ └────────────┘ └────────────┘ └────────────┘ ║
# ║ ║
# ║ BENEFITS: ║
# ║ • More precise matching (find exact relevant section) ║
# ║ • Works with embedding model limits ║
# ║ • Overlapping chunks prevent information loss at boundaries ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
def read_pdf(file_path: str) -> str:
"""
Extract all text content from a PDF file.
HOW IT WORKS:
1. Open the PDF file in binary read mode
2. Create a PDF reader to parse the file
3. Loop through each page
4. Extract text from each page
5. Add page markers [Page X] for reference
6. Combine all text into one string
ARGS:
file_path: Path to the PDF file (e.g., "data/handbook.pdf")
RETURNS:
String containing all text from the PDF
Returns empty string if there's an error
"""
try:
# Check if pypdf library is available
if PdfReader is None:
print("pypdf not installed. Install with: pip install pypdf")
return ""
# Initialize empty string to accumulate text
text = ""
# Open PDF file in binary read mode ('rb')
# Binary mode is required because PDFs are binary files
with open(file_path, 'rb') as file:
# Create PDF reader object
pdf_reader = PdfReader(file)
# Loop through each page in the PDF
# enumerate() gives us both the page number and the page object
for page_num, page in enumerate(pdf_reader.pages):
# Extract text from this page
extracted = page.extract_text()
# Only add if there's actual text (not empty)
if extracted:
# Add page marker and the extracted text
text += f"\n[Page {page_num + 1}]\n" + extracted
return text
except Exception as e:
# If anything goes wrong, print error and return empty string
print(f"Error reading PDF {file_path}: {e}")
return ""
def read_docx(file_path: str) -> str:
"""
Extract all text content from a Microsoft Word (.docx) file.
HOW IT WORKS:
1. Open the Word document using python-docx library
2. Extract text from each paragraph
3. Join paragraphs with double newlines
ARGS:
file_path: Path to the Word file (e.g., "data/syllabus.docx")
RETURNS:
String containing all text from the document
Returns empty string if there's an error
"""
try:
# Check if python-docx library is available
if Document is None:
print("python-docx not installed. Install with: pip install
python-docx")
return ""
# Open the Word document
doc = Document(file_path)
# Extract text from each paragraph and join them
# List comprehension: [para.text for each para if it has content]
# Then join all paragraphs with double newlines for readability
text = "\n\n".join([para.text for para in doc.paragraphs if
para.text.strip()])
return text
except Exception as e:
# If anything goes wrong, print error and return empty string
print(f"Error reading DOCX {file_path}: {e}")
return ""
def read_txt(file_path: str) -> str:
"""
Extract all text content from a plain text (.txt) file.
This is the simplest reader - just opens and reads the file.
ARGS:
file_path: Path to the text file (e.g., "data/notes.txt")
RETURNS:
String containing all text from the file
Returns empty string if there's an error
"""
try:
# Open file with UTF-8 encoding (supports special characters)
with open(file_path, 'r', encoding='utf-8') as file:
# Read and return entire file content
return file.read()
except Exception as e:
# If anything goes wrong, print error and return empty string
print(f"Error reading TXT {file_path}: {e}")
return ""
def read_document(file_path: str) -> str:
"""
Read a document and return its text content.
Automatically selects the correct reader based on file extension.
This is a "dispatcher" function - it looks at the file type
and calls the appropriate reader function.
SUPPORTED FORMATS:
• .pdf → Uses read_pdf()
• .docx → Uses read_docx()
• .txt → Uses read_txt()
ARGS:
file_path: Path to any supported document
RETURNS:
String containing the document text
"""
# Get file extension and convert to lowercase
# Path("file.PDF").suffix.lower() → ".pdf"
ext = Path(file_path).suffix.lower()
# Call the appropriate reader based on extension
if ext == '.pdf':
return read_pdf(file_path)
elif ext == '.docx':
return read_docx(file_path)
elif ext == '.txt':
return read_txt(file_path)
else:
# Unknown file type
print(f"Unsupported file type: {ext}")
return ""
def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int =
CHUNK_OVERLAP) -> List[str]:
"""
Split a large text into smaller, overlapping chunks.
FIXED VERSION - No more infinite loops or memory crashes!
"""
chunks = []
# Clean text first - remove visual separators and artifacts
text = re.sub(r'={3,}', '', text) # Remove ========== lines
text = re.sub(r'-{3,}', '', text) # Remove ----------
lines
text = re.sub(r'Source:\s*https?://[^\s]+', '', text) #
Remove "Source: URL" lines
# NEW: Clean up weird encoding artifacts and gibberish
text = re.sub(r'[^\x00-\x7F\u0370-\u03FF\u1F00-\u1FFF]+', '
', text) # Remove non-Latin/Greek chars
text = re.sub(r'\s+([.,!?;:])', r'\1', text) # Fix "word ." →
"word."
text = re.sub(r'([.,!?;:])\s*([.,!?;:])+', r'\1', text) #
Fix multiple punctuation
text = re.sub(r'\n{3,}', '\n\n', text) # Multiple newlines →
double newline
text = re.sub(r' {2,}', ' ', text) # Multiple spaces → single space
text_length = len(text)
# Safety check
if text_length == 0:
return []
start = 0
iteration_count = 0 # Safety counter
while start < text_length:
iteration_count += 1
# EMERGENCY BRAKE
if iteration_count > 1000:
print(f"⚠️ Breaking loop after 1000 iterations to prevent crash!")
break
# Calculate end position - NEVER exceed text length
end = min(start + chunk_size, text_length)
# Only try smart boundaries if we have room
if end < text_length and (end - start) > MIN_CHUNK_LENGTH:
# Try paragraph break
paragraph_end = text.rfind('\n\n', start + MIN_CHUNK_LENGTH, end)
if paragraph_end > start + MIN_CHUNK_LENGTH:
end = paragraph_end + 2
else:
# Try sentence ending
sentence_end = max(
text.rfind('. ', start + MIN_CHUNK_LENGTH, end),
text.rfind('! ', start + MIN_CHUNK_LENGTH, end),
text.rfind('? ', start + MIN_CHUNK_LENGTH, end),
text.rfind('.\n', start + MIN_CHUNK_LENGTH, end),
text.rfind(':\n', start + MIN_CHUNK_LENGTH, end),
)
if sentence_end > start + MIN_CHUNK_LENGTH:
end = sentence_end + 1
# Extract chunk
chunk = text[start:end].strip()
# Add chunk if valid
if len(chunk) >= MIN_CHUNK_LENGTH:
chunks.append(chunk)
elif len(chunk) > 50:
if chunks:
chunks[-1] = chunks[-1] + " " + chunk
else:
chunks.append(chunk)
# CRITICAL FIX: Always move forward by AT LEAST chunk_size - overlap
# This guarantees we make progress
old_start = start
start = end - overlap
# If we didn't move forward enough, force a jump
if start <= old_start:
start = old_start + max(chunk_size // 2, 100)
# If we're at or past the end, stop
if start >= text_length:
break
return chunks
def ingest_documents(data_folder: str = DATA_FOLDER) -> List[Dict]:
print(f"\n📂 Ingesting documents from: {data_folder}")
all_chunks = []
supported_extensions = ['.pdf', '.docx', '.txt', '.md']
files = [f for f in Path(data_folder).glob('**/*')
if f.suffix.lower() in supported_extensions]
if not files:
print(f"⚠️ No documents found in {data_folder}/")
print(f" Please add PDF, DOCX, TXT, or MD files to get started with
RAG!")
return []
for file_path in files:
print(f" 📄 Processing: {file_path.name}")
text = read_document(str(file_path))
if not text.strip():
print(f" ⚠️ Empty document, skipping...")
continue
# SAFETY: Skip extremely large files
if len(text) > 5_000_000: # 5MB of text
print(f" ⚠️ File too large ({len(text)} chars), skipping to prevent
crash...")
continue
print(f" 📏 Size: {len(text):,} characters")
chunks = chunk_text(text)
for i, chunk in enumerate(chunks):
all_chunks.append({
'text': chunk,
'source': file_path.name,
'chunk_id': i,
'total_chunks': len(chunks)
})
print(f"✅ Ingested {len(files)} documents → {len(all_chunks)}
chunks\n")
return all_chunks
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ VECTOR STORE (FAISS DATABASE) ║
# ║ ║
# ║ This is the "heart" of the RAG system - it stores and searches
documents ║
# ║ ║
# ║ WHAT IS A VECTOR STORE? ║
# ║
┌─────────────────────────────────────────────────────────────────────┐
║
# ║ │ Traditional Database: Vector Store: │ ║
# ║ │ "Find rows where "Find text with SIMILAR MEANING to │ ║
# ║ │ column = 'homework'" 'homework help assignment submit'" │ ║
# ║ │ │ ║
# ║ │ Exact match only! Understands synonyms & concepts! │ ║
# ║
└─────────────────────────────────────────────────────────────────────┘
║
# ║ ║
# ║ HOW IT WORKS: ║
# ║ 1. Each text chunk is converted to a vector (list of 384 numbers) ║
# ║ 2. Vectors are stored in FAISS (Facebook AI Similarity Search) ║
# ║ 3. When user asks a question, we convert it to a vector too ║
# ║ 4. FAISS finds the vectors closest to the question vector ║
# ║ 5. Closest vectors = most relevant text chunks ║
# ║ ║
# ║ FAISS is incredibly fast - can search millions of vectors in
milliseconds ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
class DocumentVectorStore:
"""
FAISS-based vector store for document chunks.
This class manages the entire search pipeline:
- Storing document embeddings
- Searching for relevant chunks
- Re-ranking results for accuracy
- Query expansion for better recall
"""
def __init__(self, model: SentenceTransformer):
"""
Initialize the vector store.
ARGS:
model: The SentenceTransformer model for creating embeddings
"""
self.model = model # The AI model that converts text → vectors
self.index = None # The FAISS index (will be created later)
self.chunks = [] # List to store all document chunks
self.dimension = 384 # Size of each embedding vector (MiniLM uses 384)
def build_index(self, chunks: List[Dict]):
"""
Build the FAISS search index from document chunks.
╔════════════════════════════════════════════════════════════════════════╗
║ WHAT THIS DOES (Visual Example) ║
╠════════════════════════════════════════════════════════════════════════╣
║ ║
║ INPUT: List of text chunks ║
║ ┌────────────────────────────────────────┐ ║
║ │ "Submit assignments via the portal..." │ ──┐ ║
║ │ "Office hours are Monday 2-4pm..." │ ──┼─→ ENCODE ║
║ │ "Final exam covers chapters 1-5..." │ ──┘ ║
║ └────────────────────────────────────────┘ ║
║ ↓ ║
║ OUTPUT: Numerical vectors (384 numbers each) ║
║ ┌────────────────────────────────────────┐ ║
║ │ [0.12, -0.45, 0.78, ..., 0.23] │ ← Chunk 1 vector ║
║ │ [0.34, 0.67, -0.12, ..., -0.56] │ ← Chunk 2 vector ║
║ │ [-0.23, 0.89, 0.34, ..., 0.12] │ ← Chunk 3 vector ║
║ └────────────────────────────────────────┘ ║
║ ↓ ║
║ STORED IN: FAISS Index (optimized for fast searching) ║
╚════════════════════════════════════════════════════════════════════════╝
ARGS:
chunks: List of chunk dictionaries from ingest_documents()
"""
# Handle edge case: no chunks to index
if not chunks:
print("⚠️ No chunks to index")
return
print("🔨 Building vector index...")
# Store the chunks for later retrieval
self.chunks = chunks
# ─── STEP 1: EXTRACT TEXT FROM CHUNKS ───
# Get just the text content from each chunk dictionary
texts = [chunk['text'] for chunk in chunks]
# ─── STEP 2: CONVERT TEXT TO VECTORS (EMBEDDINGS) ───
# This is where the AI model processes each text and creates vectors
# show_progress_bar=True gives a visual progress indicator
embeddings = self.model.encode(texts, show_progress_bar=True)
# ─── STEP 3: NORMALIZE VECTORS ───
# Normalization makes all vectors have "length" 1
# This allows us to use inner product (faster) instead of cosine
similarity
# Math: normalized vectors → inner product = cosine similarity
faiss.normalize_L2(embeddings)
# ─── STEP 4: CREATE FAISS INDEX ───
# IndexFlatIP = Index using Flat storage (all vectors) with Inner
Product
# self.dimension = 384 (the size of our vectors)
self.index = faiss.IndexFlatIP(self.dimension)
# ─── STEP 5: ADD VECTORS TO INDEX ───
# Convert to float32 (required by FAISS)
self.index.add(embeddings.astype('float32'))
print(f"✅ Index built with {len(chunks)} chunks\n")
def search(self, query: str, top_k: int = TOP_K_CHUNKS) ->
List[Tuple[Dict, float]]:
"""
Search for the most relevant chunks matching a query.
This is the main search function that:
1. Preprocesses the query (expands abbreviations, etc.)
2. Converts the query to a vector
3. Finds the closest chunk vectors
4. Optionally re-ranks for better accuracy
ARGS:
query: The user's question
top_k: How many results to return
RETURNS:
List of tuples: [(chunk_dict, similarity_score), ...]
Higher scores = more relevant
"""
# Handle edge case: index not built yet
if self.index is None or len(self.chunks) == 0:
return []
# ─── STEP 1: PREPROCESS QUERY ───
# Clean up and expand the query (e.g., "hw" → "homework")
processed_query = preprocess_query(query)
# ─── STEP 2: ENCODE QUERY TO VECTOR ───
# Convert the query text to a 384-dimensional vector
query_embedding = self.model.encode([processed_query])
# Normalize the query vector (same as we did for document vectors)
faiss.normalize_L2(query_embedding)
# ─── STEP 3: SEARCH THE INDEX ───
# If re-ranking is enabled, get more candidates to re-rank
search_k = top_k * 2 if USE_RERANKING else top_k
# FAISS search returns:
# - scores: similarity scores (higher = more similar)
# - indices: positions of the matching chunks in self.chunks
scores, indices = self.index.search(query_embedding.astype('float32'),
search_k)
# ─── STEP 4: COLLECT RESULTS ───
# Convert indices to actual chunk objects with their scores
results = []
for idx, score in zip(indices[0], scores[0]):
if idx < len(self.chunks): # Safety check
results.append((self.chunks[idx], float(score)))
# ─── STEP 5: OPTIONAL RE-RANKING ───
# Re-ranking improves accuracy by considering keyword matches
if USE_RERANKING and len(results) > 1:
results = self._rerank_results(processed_query, results, top_k)
else:
results = results[:top_k]
return results
def _rerank_results(self, query: str, results: List[Tuple[Dict,
float]], top_k: int) -> List[Tuple[Dict, float]]:
"""
Re-rank search results using keyword matching + semantic scores.
WHY RE-RANKING HELPS:
Pure semantic search sometimes misses exact keyword matches.
Re-ranking combines:
- Semantic similarity (70%) - understanding meaning
- Keyword matching (20%) - exact word matches
- Structure boost (10%) - bonus for lists, steps, instructions
EXAMPLE:
Query: "how to submit assignment"
Chunk A: "Uploading your work to the portal..." (semantic score:
0.85)
Chunk B: "To submit an assignment, follow..." (semantic score: 0.80)
After re-ranking, Chunk B might score higher because it has
exact keyword matches for "submit" and "assignment".
ARGS:
query: The preprocessed user query
results: Initial search results from FAISS
top_k: How many results to return
RETURNS:
Re-ranked list of results
"""
# ─── EXTRACT QUERY KEYWORDS ───
# Split query into individual words (lowercased)
query_terms = set(query.lower().split())
# Remove common words that don't help with matching (stopwords)
# These are words like "the", "a", "is" that appear everywhere
stopwords = {'the', 'a', 'an', 'is', 'are', 'was', 'were',
'to', 'of', 'in', 'for',
'on', 'with', 'how', 'what', 'where', 'when', 'why',
'can', 'do', 'i',
'το', 'η', 'ο', 'τα', 'τις', 'στο', 'στην', 'για',
'με', 'πώς', 'τι'}
query_terms = query_terms - stopwords # Remove stopwords
# ─── CALCULATE NEW SCORES ───
reranked = []
for chunk, semantic_score in results:
chunk_text_lower = chunk['text'].lower()
# Calculate keyword overlap score (0 to 1)
# How many query keywords appear in this chunk?
if query_terms:
matches = sum(1 for term in query_terms if term in chunk_text_lower)
keyword_score = matches / len(query_terms)
else:
keyword_score = 0
# Boost for exact phrase matches
# If the entire query appears in the chunk, add 0.1
phrase_boost = 0.1 if query.lower() in chunk_text_lower else 0
# Boost for chunks with structured content
# Lists and instructions are often more useful answers
structure_boost = 0
if any(marker in chunk_text_lower for marker in ['steps:', 'how
to:', '1)', '1.', '•', 'instructions']):
structure_boost = 0.05
# ─── COMBINE SCORES ───
# Weighted combination: semantic (70%) + keyword (20%) + boosts (10%)
combined_score = (semantic_score * 0.70) + (keyword_score * 0.20) +
phrase_boost + structure_boost
reranked.append((chunk, combined_score))
# Sort by combined score (highest first)
reranked.sort(key=lambda x: x[1], reverse=True)
# Return only top_k results
return reranked[:top_k]
def search_with_expansion(self, query: str, language: str = 'en',
top_k: int = TOP_K_CHUNKS) -> List[Tuple[Dict, float]]:
"""
Search with query expansion for better recall.
QUERY EXPANSION means trying multiple versions of the question:
Original: "how to submit homework"
Expanded: ["how to submit homework", ← original (weight: 1.0)
"submit homework", ← simplified (weight: 0.7)
"steps to submit homework", ← variation (weight: 0.7)
"guide for submit homework"] ← variation (weight: 0.7)
This helps catch documents that might use different wording.
ARGS:
query: The user's question
language: 'en' for English, 'el' for Greek
top_k: How many results to return
RETURNS:
Combined, deduplicated results from all query variations
"""
# Skip expansion if disabled in settings
if not USE_QUERY_EXPANSION:
return self.search(query, top_k)
# ─── GENERATE QUERY VARIATIONS ───
query_variations = expand_query(query, language)
# ─── SEARCH WITH EACH VARIATION ───
# Use a dictionary to track best score for each unique chunk
# Key = (source file, chunk_id), Value = (chunk, best_score)
all_results = {}
for i, q_var in enumerate(query_variations):
# Original query gets full weight, variations get 70%
weight = 1.0 if i == 0 else 0.7
# Search with this query variation
results = self.search(q_var, top_k)
# Process each result
for chunk, score in results:
# Create unique key for this chunk
chunk_key = (chunk['source'], chunk['chunk_id'])
# Apply weight to the score
weighted_score = score * weight
if chunk_key in all_results:
# This chunk was already found with another query variation
# Keep whichever version has the higher score
# Compare by score only (index [1]) - can't compare dicts directly
if weighted_score > all_results[chunk_key][1]:
all_results[chunk_key] = (chunk, weighted_score)
else:
# New chunk - add it to results
all_results[chunk_key] = (chunk, weighted_score)
# ─── SORT AND RETURN ───
# Sort all results by score (highest first) and return top_k
final_results = sorted(all_results.values(), key=lambda x: x[1],
reverse=True)
return final_results[:top_k]
def save_index(vector_store, chunks, filename="vector_store.pkl"):
"""
Save the vector store and chunks to disk for faster startup.
"""
try:
print(f"💾 Saving vector store to {filename}...")
data = {
'chunks': chunks,
'faiss_index': faiss.serialize_index(vector_store.index) if
vector_store.index else None,
'dimension': vector_store.dimension
}
with open(filename, 'wb') as f:
pickle.dump(data, f)
print(f"✅ Vector store saved successfully!")
return True
except Exception as e:
print(f"❌ Error saving vector store: {e}")
return False
def load_index(vector_store, filename="vector_store.pkl"):
"""
Load a previously saved vector store from disk.
Returns (chunks, success_flag)
"""
try:
if not os.path.exists(filename):
print(f"⚠️ No saved index found at {filename}")
return None, False
print(f"📂 Loading vector store from {filename}...")
with open(filename, 'rb') as f:
data = pickle.load(f)
chunks = data['chunks']
vector_store.chunks = chunks
vector_store.dimension = data['dimension']
if data['faiss_index']:
vector_store.index = faiss.deserialize_index(data['faiss_index'])
print(f"✅ Loaded {len(chunks)} chunks from saved index!")
return chunks, True
except Exception as e:
print(f"❌ Error loading vector store: {e}")
return None, False
def should_rebuild_index(data_folder=DATA_FOLDER,
index_file="vector_store.pkl"):
"""
Check if we need to rebuild the index (new/modified files).
"""
if not os.path.exists(index_file):
return True
# Get index file modification time
index_time = os.path.getmtime(index_file)
# Check if any data files are newer than the index
supported_extensions = ['.pdf', '.docx', '.txt', '.md']
files = [f for f in Path(data_folder).glob('**/*')
if f.suffix.lower() in supported_extensions]
for file in files:
if os.path.getmtime(file) > index_time:
print(f"📝 Detected new/modified file: {file.name}")
return True
return False
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ INITIALIZE VECTOR STORE AND LOAD DOCUMENTS ║
# ║ ║
# ║ This code runs once when the application starts. ║
# ║ It reads all documents and builds the search index. ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# Create the vector store instance with our semantic model
vector_store = DocumentVectorStore(semantic_model)
# Check if we should rebuild or can load from cache
INDEX_FILE = "vector_store.pkl"
if should_rebuild_index(DATA_FOLDER, INDEX_FILE):
print("\n🔄 Building new index (new/modified documents
detected)...")
# Read all documents from the data folder and build the search index
document_chunks = ingest_documents()
vector_store.build_index(document_chunks)
# Save for next time
save_index(vector_store, document_chunks, INDEX_FILE)
else:
print("\n⚡ Loading cached index (much faster!)...")
document_chunks, success = load_index(vector_store, INDEX_FILE)
if not success:
print("🔄 Falling back to rebuilding index...")
document_chunks = ingest_documents()
vector_store.build_index(document_chunks)
save_index(vector_store, document_chunks, INDEX_FILE)
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ FAQ KNOWLEDGE BASE (FALLBACK) ║
# ║ ║
# ║ The FAQ system provides pre-written answers to common questions. ║
# ║ ║
# ║ WHEN IT'S USED: ║
# ║ • User asks a common question that matches an FAQ ║
# ║ • Documents don't contain a good answer ║
# ║ • Quick responses without document search ║
# ║ ║
# ║ HOW IT WORKS: ║
# ║ 1. FAQs are stored in separate files (knowledge_base_en.py,
_el.py) ║
# ║ 2. Each FAQ has multiple question variations and one answer ║
# ║ 3. We pre-compute embeddings for all FAQ questions at startup ║
# ║ 4. When user asks, we find the most similar FAQ question ║
# ║ 5. If similarity > threshold (60%), we return the FAQ answer ║
# ║ ║
# ║ SUPPORTS: English ('en') and Greek ('el') ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
# ─── IMPORT FAQ DATA FROM EXTERNAL FILES ───
# FAQs are stored in separate files for easier maintenance
# knowledge_base_en.py contains English FAQs
# knowledge_base_el.py contains Greek FAQs
from knowledge_base_en import KNOWLEDGE_BASE_EN
from knowledge_base_el import KNOWLEDGE_BASE_EL
# Combine both knowledge bases into one dictionary
# Structure: {'en': [list of EN FAQs], 'el': [list of EL FAQs]}
KNOWLEDGE_BASE = {
'en': KNOWLEDGE_BASE_EN,
'el': KNOWLEDGE_BASE_EL
}
# ─── PRE-COMPUTE FAQ EMBEDDINGS ───
# Instead of encoding FAQ questions every time a user asks something,
# we encode them once at startup and store the vectors.
# This makes FAQ matching much faster!
print("[4/4] Computing FAQ embeddings...")
# Dictionaries to store embeddings and Q&A mappings for each language
faq_embeddings = {} # {language: numpy array of embeddings}
faq_qa_pairs = {} # {language: list of {answer, idx} dicts}
# Process each language
for lang in ['en', 'el']:
all_questions = [] # List of all FAQ questions
qa_map = [] # Mapping from question index to answer
# Loop through each FAQ entry
for idx, item in enumerate(KNOWLEDGE_BASE[lang]):
# Each FAQ item has multiple question variations
for question in item['questions']:
all_questions.append(question)
# Store which answer this question maps to
qa_map.append({'answer': item['answer'], 'idx': idx})
# Encode all questions if there are any
if all_questions:
embeddings = semantic_model.encode(all_questions)
faq_embeddings[lang] = embeddings
faq_qa_pairs[lang] = qa_map
print(" ✓ FAQ embeddings computed!")
print("="*70)
print("✅ SYSTEM READY! You can now start the web server.")
print("="*70 + "\n")
def _match_faq_in_language(user_input: str, language: str) -> Dict:
"""
Internal helper function to find matching FAQ in a specific language.
This is a private function (starts with _) used by get_faq_response().
HOW IT WORKS:
1. Encode the user's question into a vector
2. Compare with all pre-computed FAQ question vectors
3. Find the most similar FAQ question
4. If similarity > threshold, return the answer
ARGS:
user_input: The user's question
language: Which FAQ language to search ('en', 'el', or
'greeklish')
RETURNS:
Dictionary with answer, confidence, etc. if match found
None if no good match
"""
# Map Greeklish to Greek FAQ (we don't have separate Greeklish FAQ)
faq_lang = 'el' if language == 'greeklish' else language
# Check if we have FAQ embeddings for this language
if faq_lang not in faq_embeddings or len(faq_embeddings[faq_lang]) ==
0:
return None
# Encode the user's question into a vector
user_embedding = semantic_model.encode([user_input])
# Calculate similarity between user question and all FAQ questions
# cosine_similarity returns values from -1 to 1 (higher = more similar)
similarities = cosine_similarity(user_embedding,
faq_embeddings[faq_lang])[0]
# Find the FAQ question with highest similarity
best_idx = np.argmax(similarities) # Index of best match
best_score = float(similarities[best_idx]) # Similarity score
# Only return if similarity exceeds our threshold (60%)
if best_score >= FAQ_CONFIDENCE_THRESHOLD:
# Get the answer for this FAQ
answer = faq_qa_pairs[faq_lang][best_idx]['answer']
return {
'answer': answer, # The FAQ answer text
'confidence': best_score, # How confident we are (0-1)
'method': 'FAQ', # How we found this answer
'faq_language': faq_lang # Which FAQ language matched
}
# No good match found
return None
def get_faq_response(user_input: str, language: str = 'en') -> Dict:
"""
Try to answer the user's question using the FAQ knowledge base.
SEARCH STRATEGY:
1. First, search in the user's language (en or el)
2. If no match found and user spoke English, try Greek FAQs
(our multilingual model can match English questions to Greek FAQs!)
ARGS:
user_input: The user's question
language: User's interface language ('en' or 'el')
RETURNS:
Dictionary with answer if FAQ match found
None if no match
"""
# ─── STEP 1: SEARCH PRIMARY LANGUAGE ───
# Try to find an FAQ match in the user's language
primary_result = _match_faq_in_language(user_input, language)
if primary_result:
return primary_result
# ─── STEP 2: FALLBACK FOR ENGLISH USERS ───
# If user is speaking English and we didn't find a match,
# try the Greek FAQs (the multilingual model can handle this!)
if language == 'en':
fallback_language = 'el'
fallback_result = _match_faq_in_language(user_input, fallback_language)
if fallback_result:
# Add a note that this answer came from Greek FAQ
fallback_result['answer'] = (
"ℹ️ This answer comes from the Greek knowledge base:\n\n"
\+ fallback_result['answer']
)
return fallback_result
# No match in either primary or fallback FAQ
return None
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ RAG RESPONSE GENERATION ║
# ║ ║
# ║ This section contains the main response generation logic. ║
# ║ ║
# ║ RESPONSE HIERARCHY (Fallback Chain): ║
# ║
┌─────────────────────────────────────────────────────────────────────┐
║
# ║ │ 1. 📄 DOCUMENT SEARCH (RAG) │ ║
# ║ │ → Search your documents for relevant information │ ║
# ║ │ → If found with confidence > 35%, use document answer │ ║
# ║ │ ↓ (if no match) │ ║
# ║ │ 2. ❓ FAQ KNOWLEDGE BASE │ ║
# ║ │ → Check if question matches a predefined FAQ │ ║
# ║ │ → If match with confidence > 60%, use FAQ answer │ ║
# ║ │ ↓ (if no match) │ ║
# ║ │ 3. 🤖 AI LANGUAGE MODEL (TinyLlama) │ ║
# ║ │ → Use AI to generate an answer from general knowledge │ ║
# ║ │ → Marked with warning since it's not from your documents │ ║
# ║ │ ↓ (if AI not available) │ ║
# ║ │ 4. 🤷 FALLBACK MESSAGE │ ║
# ║ │ → Apologize and suggest rephrasing the question │ ║
# ║
└─────────────────────────────────────────────────────────────────────┘
║
#
╚══════════════════════════════════════════════════════════════════════════════╝
def extract_answer_from_chunks(query: str, chunks: List[Tuple[Dict,
float]], language: str = 'en') -> Dict:
# Handle empty input
if not chunks:
return None
# ─── FILTER CHUNKS BY LANGUAGE ───
# Keep only chunks from files matching the user's language
if language == 'en':
# Keep only English docs (files in /en/ folder or no language prefix)
filtered_chunks = [(chunk, score) for chunk, score in chunks
if '/en/' in chunk['source'] or
(not chunk['source'].startswith('el') and '_el' not in
chunk['source'].lower() and 'greeklish' not in
chunk['source'].lower())]
elif language == 'greeklish':
# Keep only Greeklish docs (files in /el_greeklish/ folder)
filtered_chunks = [(chunk, score) for chunk, score in chunks
if 'el_greeklish' in chunk['source'] or 'greeklish' in
chunk['source'].lower()]
else: # language == 'el'
# Keep only Greek docs (files in /el/ folder, but NOT el_greeklish)
filtered_chunks = [(chunk, score) for chunk, score in chunks
if ('/el/' in chunk['source'] or
chunk['source'].startswith('el'))
and 'greeklish' not in chunk['source'].lower()]
# If filtering removed all chunks, use original (better than nothing)
if not filtered_chunks:
filtered_chunks = chunks
chunks = filtered_chunks # Replace chunks with filtered version
# Continue with rest of function...
sources = []
best_chunk, best_score = chunks[0]
# ─── SMART CONTEXT AGGREGATION ───
# Start with the best chunk's text
aggregated_text = best_chunk['text']
# Track which chunks we've used (to avoid duplicates)
used_chunks = {(best_chunk['source'], best_chunk['chunk_id'])}
# Process each chunk
for i, (chunk, score) in enumerate(chunks):
# Add to sources list
sources.append({
'file': chunk['source'], # Filename
'chunk': chunk['chunk_id'] + 1, # Human-readable chunk number
'score': f"{score:.2%}", # Format score as percentage
'preview': chunk['text'][:150] + "..." # First 150 chars
})
# ─── TRY TO AGGREGATE ADJACENT CHUNKS ───
# If this chunk is good enough and from the same file as a used chunk,
# and it's right before or after, we can combine them
if i > 0 and score >= DOCUMENT_CONFIDENCE_THRESHOLD * 0.9:
chunk_key = (chunk['source'], chunk['chunk_id'])
if chunk_key not in used_chunks:
# Check if this chunk is adjacent to any chunk we've used
is_adjacent = any(
chunk['source'] == src and abs(chunk['chunk_id'] - cid) == 1
for src, cid in used_chunks
)
# Add if adjacent and we haven't aggregated too much text
if is_adjacent and len(aggregated_text) < 1500:
# Put earlier chunks before, later chunks after
if chunk['chunk_id'] < best_chunk['chunk_id']:
aggregated_text = chunk['text'] + "\n\n" + aggregated_text
else:
aggregated_text = aggregated_text + "\n\n" + chunk['text']
used_chunks.add(chunk_key)
# The answer text is our aggregated content
answer_text = aggregated_text
# Clean up any remaining artifacts
answer_text = re.sub(r'={3,}', '', answer_text) # Remove ======
answer_text = re.sub(r'-{3,}', '', answer_text) # Remove
------
answer_text = re.sub(r'Source:\s*https?://[^\s]+', '',
answer_text) # Remove Source: URLs
answer_text = re.sub(r'\n{3,}', '\n\n', answer_text) # Clean up
extra newlines
# ─── HIGHLIGHT MOST RELEVANT SENTENCE ───
# Find the sentence that best matches the user's query
# Extract meaningful query terms (remove common words)
query_terms = set(preprocess_query(query).lower().split()) - {'the',
'a', 'an', 'is', 'to', 'how', 'what'}
# Split text into sentences
sentences = re.split(r'[.!?]\s+', answer_text)
# Find sentence with most query term matches
best_sentence = None
best_match_count = 0
for sentence in sentences:
# Only consider meaningful sentences (> 30 chars)
if len(sentence) > 30:
# Count how many query terms appear in this sentence
matches = sum(1 for term in query_terms if term in sentence.lower())
if matches > best_match_count:
best_match_count = matches
best_sentence = sentence
# If we found a highly relevant sentence that's not already at the
start,
# add it as a highlighted "Key point" at the top
if best_sentence and best_match_count >= 2 and best_sentence not in
answer_text[:200]:
answer_text = f"**Key point:**
{best_sentence.strip()}\n\n---\n\n{answer_text}"
# ─── ADD SOURCE CITATIONS ───
if language == 'en':
citations = f"\n\n📚 Sources:\n"
for i, src in enumerate(sources[:TOP_K_FINAL], 1):
citations += f"{i}. {src['file']} (Chunk {src['chunk']},
Relevance: {src['score']})\n"
else:
citations = f"\n\n📚 Πηγές:\n"
for i, src in enumerate(sources[:TOP_K_FINAL], 1):
citations += f"{i}. {src['file']} (Τμήμα {src['chunk']},
Σχετικότητα: {src['score']})\n"
return {
'answer': answer_text + citations, # Full formatted answer
'sources': sources, # Source list for reference
'confidence': best_score, # How confident we are
'method': 'RAG', # How we found this answer
'chunks_used': len(used_chunks) # How many chunks we combined
}
def get_ai_response(user_input: str, context_chunks: List[Tuple[Dict,
float]], language: str = 'en') -> str:
"""
Generate an answer using the TinyLlama AI model.
This is used as a fallback when documents and FAQs don't have an
answer.
The AI can provide general knowledge responses.
HOW IT WORKS:
1. Build a prompt with available context from document chunks
2. Ask TinyLlama to answer based on the context
3. Return the generated response
ARGS:
user_input: The user's question
context_chunks: Any relevant chunks found (may be low confidence)
language: 'en' or 'el' for language of response
RETURNS:
Generated answer string, or None if AI fails
"""
# Check if AI is available
if not USE_AI_FALLBACK or ai_pipeline is None:
return None
try:
# ─── BUILD CONTEXT ───
# Include any document chunks we found (even if low confidence)
if context_chunks:
context = "\n".join([f"- {chunk['text'][:200]}"
for chunk, score in context_chunks[:2]])
else:
context = "No specific context available."
# ─── CREATE PROMPT ───
# TinyLlama uses a specific chat format with <\|system\|>,
<\|user\|>, <\|assistant\|>
if language == 'en':
prompt = f"""<\|system\|>You are a helpful assistant for Open
eClass LMS. Answer briefly in 2-3 sentences.</s>
<\|user\|>
Context: {context}
Question: {user_input}</s>
<\|assistant\|>"""
else:
prompt = f"""<\|system\|>Είσαι βοηθός για το Open eClass. Απάντησε
σύντομα σε 2-3 προτάσεις.</s>
<\|user\|>
Πλαίσιο: {context}
Ερώτηση: {user_input}</s>
<\|assistant\|>"""
# ─── GENERATE RESPONSE ───
# Use the pipeline for fast inference
response = ai_pipeline(
prompt,
max_new_tokens=80, # Limit response length
do_sample=True, # Enable sampling for variety
temperature=0.7, # Controls randomness (0=deterministic, 1=creative)
top_p=0.9, # Nucleus sampling (consider top 90% probability mass)
return_full_text=False # Only return generated text, not the prompt
)
# Extract and clean the answer
answer = response[0]['generated_text'].strip()
return answer[:400] # Limit response length
except Exception as e:
print(f"AI model error: {e}")
return None
def get_rag_response(user_input: str, language: str = 'en') -> str:
"""
═══════════════════════════════════════════════════════════════════════════════
║ MAIN RAG PIPELINE ║
║ ║
║ This is the main function that handles all user questions. ║
║ It orchestrates the entire response generation process. ║
═══════════════════════════════════════════════════════════════════════════════
PIPELINE STEPS:
0. Check cache - Return cached response if available
1. Safety check - Block harmful queries
2. Gibberish detection - Block nonsense input
... (rest of your docstring)
"""
# Log the incoming query
print(f"\n[QUERY] {user_input}")
# ═══ STEP -2: SAFETY CHECK FIRST (BEFORE LANGUAGE DETECTION) ═══
# Safety check with user's preferred language for block messages
safety_check = check_harmful_content(user_input, language)
if not safety_check['is_safe']:
print(f"[SAFETY] Query blocked - Category:
{safety_check['category']}, Severity:
{safety_check['severity']}")
response = safety_check['block_message']
return response # Don't cache harmful queries
# ═══ STEP -1: DETECT & VALIDATE LANGUAGE ═══
detected_lang = detect_language(user_input)
print(f"[LANGUAGE] Detected: {detected_lang}")
# Block unsupported languages
if detected_lang == 'unsupported':
print(f"[LANGUAGE BLOCK] Unsupported language detected")
return get_language_block_message(language)
# Auto-switch language based on detection
response_language = language # Start with user's preference
if detected_lang == 'el':
response_language = 'el'
print(f"[LANGUAGE] Switched to Greek")
elif detected_lang == 'greeklish':
response_language = 'greeklish' # Use Greeklish documents
print(f"[LANGUAGE] Detected Greeklish → Using Greeklish responses")
else:
response_language = 'en'
print(f"[LANGUAGE] Using English")
# ═══ STEP 0: CHECK CACHE ═══
cached_response = get_cached_response(user_input, response_language)
if cached_response:
return cached_response
# ═══ STEP 0.5: GIBBERISH CHECK ═══
if is_gibberish(user_input):
print(f"[GIBBERISH] Query detected as gibberish")
if response_language == 'en':
response = "❓ I didn't quite understand that. Could you please
rephrase your question? I'm here to help with Open eClass queries!"
else:
response = "❓ Δεν το κατάλαβα αυτό. Μπορείτε να αναδιατυπώσετε την
ερώτησή σας; Είμαι εδώ για να βοηθήσω με ερωτήσεις για το Open eClass!"
cache_response(user_input, response_language, response)
return response
# ═══ STEP 1: PREPROCESS QUERY ═══
processed_input = preprocess_query(user_input)
print(f"[PREPROCESSED] {processed_input}")
# ═══ STEP 2: SEARCH DOCUMENTS (RAG) ═══
retrieved_chunks = vector_store.search_with_expansion(processed_input,
response_language, top_k=TOP_K_CHUNKS)
if retrieved_chunks and retrieved_chunks[0][1] >=
DOCUMENT_CONFIDENCE_THRESHOLD:
print(f"[RAG] Found {len(retrieved_chunks)} relevant chunks (best:
{retrieved_chunks[0][1]:.2%})")
result = extract_answer_from_chunks(user_input, retrieved_chunks,
response_language)
if result:
if response_language == 'en':
response = f"📄 **Retrieved from
documents:**\n\n{result['answer']}"
else:
response = f"📄 **Ανακτήθηκε από
έγγραφα:**\n\n{result['answer']}"
cache_response(user_input, response_language, response)
return response
print(f"[RAG] No high-confidence documents found")
# ═══ STEP 3: TRY FAQ KNOWLEDGE BASE ═══
faq_result = get_faq_response(user_input, response_language)
if faq_result:
print(f"[FAQ] Match found (confidence:
{faq_result['confidence']:.2%}, lang:
{faq_result.get('faq_language', response_language)})")
response = f"❓ {faq_result['answer']}"
cache_response(user_input, response_language, response)
return response
else:
print(f"[FAQ] No match found")
# ═══ STEP 4: TRY AI MODEL (TINYLLAMA) ═══
if USE_AI_FALLBACK:
print(f"[AI] Trying TinyLlama AI model...")
ai_answer = get_ai_response(user_input, retrieved_chunks or [],
response_language)
if ai_answer:
print(f"[AI] Generated response successfully")
response = f"🤖 {ai_answer}"
cache_response(user_input, response_language, response)
return response
else:
print(f"[AI] AI could not generate a response")
# ═══ STEP 5: WEB SEARCH FALLBACK ═══
print(f"[WEB SEARCH] Searching Open eClass documentation...")
try:
encoded_query = urllib.parse.quote(user_input)
search_url =
f"https://docs.openeclass.org/?do=search&q={encoded_query}"
if response_language == 'en':
response = (
"I couldn't find specific information in the loaded documents.\n\n"
"🔍 **Try searching the Open eClass documentation:**\n"
f"{search_url}\n\n"
"💡 **Other options:**\n"
"• Rephrase your question with different keywords\n"
"• Contact your system administrator\n"
"• Visit the Open eClass support forum"
)
else:
response = (
"Δεν βρήκα συγκεκριμένες πληροφορίες στα φορτωμένα έγγραφα.\n\n"
"🔍 **Δοκιμάστε αναζήτηση στην τεκμηρίωση του Open eClass:**\n"
f"{search_url}\n\n"
"💡 **Άλλες επιλογές:**\n"
"• Αναδιατυπώστε την ερώτησή σας με διαφορετικές λέξεις-κλειδιά\n"
"• Επικοινωνήστε με τον διαχειριστή συστήματος\n"
"• Επισκεφθείτε το φόρουμ υποστήριξης του Open eClass"
)
except Exception as e:
print(f"[WEB SEARCH ERROR] {e}")
if response_language == 'en':
response = "I couldn't find information about that. Please try
rephrasing your question or contact support."
else:
response = "Δεν βρήκα πληροφορίες γι' αυτό. Παρακαλώ δοκιμάστε να
αναδιατυπώσετε την ερώτησή σας ή επικοινωνήστε με την υποστήριξη."
cache_response(user_input, response_language, response)
return response
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ FLASK WEB ROUTES ║
# ║ ║
# ║ These routes define the web interface for the chatbot. ║
# ║ ║
# ║ ENDPOINTS: ║
# ║ • GET / → Home page (chat interface) ║
# ║ • POST /chat → API endpoint for chat messages ║
# ║ ║
# ║ HOW IT WORKS: ║
# ║ 1. User opens localhost:5000 in browser → sees chat interface ║
# ║ 2. User types a message and clicks send ║
# ║ 3. JavaScript sends POST request to /chat with the message ║
# ║ 4. Flask calls get_rag_response() to generate answer ║
# ║ 5. Response is sent back as JSON ║
# ║ 6. JavaScript displays the response in the chat ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
@app.route('/')
def home():
"""
Serve the main chat interface (home page).
This renders the index.html template with some statistics
to show users how many documents are loaded.
RETURNS:
HTML page with the chat interface
"""
# Count unique source documents
doc_count = len(set([c['source'] for c in document_chunks]))
# Count total chunks
chunk_count = len(document_chunks)
# Render the template with these values
# The template can display: "Loaded X documents with Y chunks"
return render_template('index.html', doc_count=doc_count,
chunk_count=chunk_count)
@app.route('/chat', methods=['POST'])
def chat():
"""
API endpoint to handle chat messages with auto language detection.
"""
# Parse the incoming JSON data
data = request.json
# Extract message and language (default to English)
user_message = data.get('message', '')
language = data.get('language', 'en') # User's preferred language
for UI
# Language will be auto-detected inside get_rag_response()
# Just pass the user's preference for fallback messages
response = get_rag_response(user_message, language)
# Return response as JSON
return jsonify({'response': response})
## What this does:
#*✅ **Auto-detects** English, Greek, and Greeklish
#✅ **Automatically switches** response language to match user's
input
#✅ **Blocks** all other languages (Arabic, Chinese, French,
Spanish, etc.)
#✅ **Greeklish support**: "pws mporo na kanw submit?" → answers
in Greek
#✅ **Safety**: Prevents curse words in languages you haven't
filtered
## Test examples:
#`User: "How do I submit homework?"
#→ Detected: English → Responds in English
#User: "Πώς κάνω submit την εργασία;"
#→ Detected: Greek → Responds in Greek
#User: "pws kano submit tin ergasia?"
#→ Detected: Greeklish → Responds in Greek
#User: "كيف أقدم الواجب؟" (Arabic)
#→ Blocked: "Sorry, I only support English and Greek"
#User: "Comment soumettre?" (French)
#→ Blocked: "Sorry, I only support English and Greek"
#
#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║ MAIN ENTRY POINT ║
# ║ ║
# ║ This code runs when you execute: python RAG.py ║
# ║ ║
# ║ It prints system information and starts the Flask web server. ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
if __name__ == "__main__":
# ─── PRINT STARTUP BANNER ───
# Show information about the loaded system
print("\n" + "="*70)
print("🚀 TRUE RAG SYSTEM - LMS Chatbot with Document Retrieval")
print("="*70)
# Show which models are loaded
print("📚 Semantic Model: paraphrase-multilingual-MiniLM-L12-v2")
print("🔍 Vector Store: FAISS")
# Show document statistics
print(f"📄 Documents Indexed: {len(set([c['source'] for c in
document_chunks]))}")
print(f"📦 Total Chunks: {len(document_chunks)}")
# Show AI status
print(f"🤖 AI Fallback: {'✅ TinyLlama Enabled' if USE_AI_FALLBACK
else '❌ Disabled'}")
print("="*70)
# ─── SHOW ACCURACY SETTINGS ───
print("\n🎯 Accuracy Enhancements:")
print(f" • Query Expansion: {'✅ Enabled' if USE_QUERY_EXPANSION else
'❌ Disabled'}")
print(f" • Re-ranking: {'✅ Enabled' if USE_RERANKING else '❌
Disabled'}")
print(f" • Chunk Size: {CHUNK_SIZE} chars (overlap: {CHUNK_OVERLAP})")
print(f" • Retrieval: Top-{TOP_K_CHUNKS} → Re-rank →
Top-{TOP_K_FINAL}")
# ─── EXPLAIN THE PIPELINE ───
print("\n💡 How it works:")
print(" 1️⃣ Preprocesses & expands query for better matching")
print(" 2️⃣ Searches document corpus using vector similarity")
print(" 3️⃣ Re-ranks results using hybrid (semantic + keyword)
scoring")
print(" 4️⃣ Aggregates adjacent chunks for complete answers")
print(" 5️⃣ Falls back to FAQ if no documents match (EN→EL when
needed)")
print(" 6️⃣ Falls back to TinyLlama AI for complex queries (if
enabled)")
# ─── SHOW HELPFUL HINTS ───
print("\n📂 Add documents to './data/' folder (PDF, DOCX, TXT)")
print("🌐 Open your browser: http://localhost:5000")
print("\n" + "="*70 + "\n")
# ─── START THE WEB SERVER ───
# debug=True enables auto-reload when code changes
# port=5000 means access via http://localhost:5000
app.run(debug=True, port=5000)
