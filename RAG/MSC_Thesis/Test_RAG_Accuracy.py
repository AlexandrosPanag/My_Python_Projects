# test_rag_accuracy.py
# RAG System Accuracy Evaluation Suite
# Tests across multiple difficulty levels: Basic, Medium, Vague, and
Hard
"""
RAG ACCURACY EVALUATION SUITE
==============================
This script tests the RAG system with questions of varying difficulty.
It measures response quality, relevance, and the system's ability to
handle different types of queries.
Usage:
    python test_rag_accuracy.py
Requirements:
    - RAG.py must be in the same directory
    - Knowledge base files must be present
"""
import sys
import time
from typing import List, Dict, Tuple
from datetime import datetime
# Import the RAG system components
try:
    from RAG import (
        get_rag_response,
        vector_store,
        preprocess_query,
        expand_query,
        DOCUMENT_CONFIDENCE_THRESHOLD,
        FAQ_CONFIDENCE_THRESHOLD,
        USE_QUERY_EXPANSION,
        USE_RERANKING
    )
    print("✅ RAG system imported successfully!\n")
except ImportError as e:
    print(f"❌ Error importing RAG system: {e}")
    print("Make sure RAG.py is in the same directory.")
    sys.exit(1)
#============================================================================
# TEST QUESTIONS BY DIFFICULTY LEVEL
#============================================================================
# BASIC QUESTIONS (Easy - Direct matches expected)
# These should have high confidence matches in FAQ or documents
BASIC_QUESTIONS = [
    {
        "id": "B1",
        "question_en": "How do I log in?",
        "question_el": "Πώς κάνω σύνδεση;",
        "expected_topics_en": ["login", "username", "password",
"sign in"],
        "expected_topics_el": ["σύνδεση", "username",
"password", "κωδικό", "όνομα χρήστη"],
        "difficulty": "BASIC",
        "notes": "Direct FAQ match expected"
    },
    {
        "id": "B2",
        "question_en": "How do I create a student account?",
        "question_el": "Πώς δημιουργώ λογαριασμό φοιτητή;",
        "expected_topics_en": ["student", "account",
"register", "registration"],
        "expected_topics_el": ["φοιτητή", "λογαριασμό",
"εγγραφή", "δημιουργία"],
        "difficulty": "BASIC",
        "notes": "Clear account creation query"
    },
    {
        "id": "B3",
        "question_en": "What is the portfolio?",
        "question_el": "Τι είναι το portfolio;",
        "expected_topics_en": ["portfolio", "courses",
"homepage", "dashboard"],
        "expected_topics_el": ["portfolio", "χαρτοφυλάκιο",
"μαθήματα", "αρχική"],
        "difficulty": "BASIC",
        "notes": "Definition question"
    },
    {
        "id": "B4",
        "question_en": "How do I submit an assignment?",
        "question_el": "Πώς υποβάλλω μια εργασία;",
        "expected_topics_en": ["assignment", "submit",
"upload", "deadline"],
        "expected_topics_el": ["εργασία", "υποβολή",
"ανέβασμα", "προθεσμία"],
        "difficulty": "BASIC",
        "notes": "Common student action"
    },
    {
        "id": "B5",
        "question_en": "Where can I find my courses?",
        "question_el": "Πού μπορώ να βρω τα μαθήματά μου;",
        "expected_topics_en": ["courses", "my courses", "course
list", "enrolled"],
        "expected_topics_el": ["μαθήματα", "μαθήματά μου",
"εγγεγραμμένος", "λίστα"],
        "difficulty": "BASIC",
        "notes": "Navigation question"
    },
    {
        "id": "B6",
        "question_en": "How do I enroll in a course?",
        "question_el": "Πώς εγγράφομαι σε ένα μάθημα;",
        "expected_topics_en": ["enroll", "register", "course",
"join"],
        "expected_topics_el": ["εγγραφή", "μάθημα",
"εγγράφομαι", "συμμετοχή"],
        "difficulty": "BASIC",
        "notes": "Course enrollment"
    },
    {
        "id": "B7",
        "question_en": "How do I upload a file?",
        "question_el": "Πώς ανεβάζω ένα αρχείο;",
        "expected_topics_en": ["upload", "file", "document",
"add"],
        "expected_topics_el": ["ανέβασμα", "αρχείο", "έγγραφο",
"προσθήκη"],
        "difficulty": "BASIC",
        "notes": "File upload question"
    },
    {
        "id": "B8",
        "question_en": "How do I download course materials?",
        "question_el": "Πώς κατεβάζω υλικό μαθήματος;",
        "expected_topics_en": ["download", "materials",
"documents", "files"],
        "expected_topics_el": ["κατέβασμα", "υλικό", "έγγραφα",
"αρχεία"],
        "difficulty": "BASIC",
        "notes": "Download materials"
    },
    {
        "id": "B9",
        "question_en": "How do I change my password?",
        "question_el": "Πώς αλλάζω τον κωδικό μου;",
        "expected_topics_en": ["change", "password", "update",
"security"],
        "expected_topics_el": ["αλλαγή", "κωδικό", "ενημέρωση",
"ασφάλεια"],
        "difficulty": "BASIC",
        "notes": "Password change"
    },
    {
        "id": "B10",
        "question_en": "How do I send a message?",
        "question_el": "Πώς στέλνω μήνυμα;",
        "expected_topics_en": ["message", "send", "inbox",
"communication"],
        "expected_topics_el": ["μήνυμα", "αποστολή",
"εισερχόμενα", "επικοινωνία"],
        "difficulty": "BASIC",
        "notes": "Messaging feature"
    },
    {
        "id": "B11",
        "question_en": "What is the calendar?",
        "question_el": "Τι είναι το ημερολόγιο;",
        "expected_topics_en": ["calendar", "schedule",
"events", "deadlines"],
        "expected_topics_el": ["ημερολόγιο", "πρόγραμμα",
"γεγονότα", "προθεσμίες"],
        "difficulty": "BASIC",
        "notes": "Calendar feature"
    },
    {
        "id": "B12",
        "question_en": "How do I take an exercise/quiz?",
        "question_el": "Πώς κάνω μια άσκηση;",
        "expected_topics_en": ["exercise", "quiz", "test",
"attempt"],
        "expected_topics_el": ["άσκηση", "τεστ", "προσπάθεια",
"εξέταση"],
        "difficulty": "BASIC",
        "notes": "Quiz/exercise feature"
    },
    {
        "id": "B13",
        "question_en": "How do I view my grades?",
        "question_el": "Πώς βλέπω τους βαθμούς μου;",
        "expected_topics_en": ["grades", "score", "results",
"gradebook"],
        "expected_topics_el": ["βαθμοί", "σκορ",
"αποτελέσματα", "βαθμολόγιο"],
        "difficulty": "BASIC",
        "notes": "Grade viewing"
    },
    {
        "id": "B14",
        "question_en": "How do I access the forum?",
        "question_el": "Πώς μπαίνω στο φόρουμ;",
        "expected_topics_en": ["forum", "discussion", "post",
"topic"],
        "expected_topics_el": ["φόρουμ", "συζήτηση",
"δημοσίευση", "θέμα"],
        "difficulty": "BASIC",
        "notes": "Forum access"
    },
    {
        "id": "B15",
        "question_en": "How do I log out?",
        "question_el": "Πώς κάνω αποσύνδεση;",
        "expected_topics_en": ["logout", "sign out", "exit",
"leave"],
        "expected_topics_el": ["αποσύνδεση", "έξοδος",
"αποχώρηση"],
        "difficulty": "BASIC",
        "notes": "Logout question"
    },
]
# MEDIUM QUESTIONS (Moderate - May require some inference)
# These require understanding context or combining information
MEDIUM_QUESTIONS = [
    {
        "id": "M1",
        "question_en": "I forgot my password, what should I do?",
        "question_el": "Ξέχασα τον κωδικό μου, τι πρέπει να κάνω;",
        "expected_topics_en": ["password", "forgot", "reset",
"recovery", "email"],
        "expected_topics_el": ["κωδικό", "ξέχασα", "επαναφορά",
"ανάκτηση", "email"],
        "difficulty": "MEDIUM",
        "notes": "Problem-solving query"
    },
    {
        "id": "M2",
        "question_en": "How can I communicate with my professor?",
        "question_el": "Πώς μπορώ να επικοινωνήσω με τον καθηγητή
μου;",
        "expected_topics_en": ["message", "forum",
"communication", "contact", "instructor"],
        "expected_topics_el": ["μήνυμα", "συζήτηση",
"επικοινωνία", "επαφή", "καθηγητή"],
        "difficulty": "MEDIUM",
        "notes": "Multiple possible answers (messages, forums,
etc.)"
    },
    {
        "id": "M3",
        "question_en": "What is Turnitin and how does it work?",
        "question_el": "Τι είναι το Turnitin και πώς λειτουργεί;",
        "expected_topics_en": ["turnitin", "plagiarism",
"similarity", "check"],
        "expected_topics_el": ["turnitin", "λογοκλοπή",
"ομοιότητα", "έλεγχο"],
        "difficulty": "MEDIUM",
        "notes": "Feature explanation with process"
    },
    {
        "id": "M4",
        "question_en": "How do I join a user group and participate in
discussions?",
        "question_el": "Πώς μπαίνω σε ομάδα χρηστών και συμμετέχω σε
συζητήσεις;",
        "expected_topics_en": ["group", "enroll", "discussion",
"forum", "participate"],
        "expected_topics_el": ["ομάδα", "εγγραφή", "συζήτηση",
"forum", "συμμετοχή"],
        "difficulty": "MEDIUM",
        "notes": "Multi-step process question"
    },
    {
        "id": "M5",
        "question_en": "What's the difference between open and
closed courses?",
        "question_el": "Ποια είναι η διαφορά μεταξύ ανοικτών και
κλειστών μαθημάτων;",
        "expected_topics_en": ["access", "open", "closed",
"registration", "type"],
        "expected_topics_el": ["πρόσβαση", "ανοικτ", "κλειστ",
"εγγραφή", "τύπος"],
        "difficulty": "MEDIUM",
        "notes": "Comparison question"
    },
    {
        "id": "M6",
        "question_en": "How do I create a new topic in the forum?",
        "question_el": "Πώς δημιουργώ νέο θέμα στο φόρουμ;",
        "expected_topics_en": ["forum", "topic", "create",
"post", "new"],
        "expected_topics_el": ["φόρουμ", "θέμα", "δημιουργία",
"δημοσίευση", "νέο"],
        "difficulty": "MEDIUM",
        "notes": "Forum topic creation"
    },
    {
        "id": "M7",
        "question_en": "How can I see who else is enrolled in my
course?",
        "question_el": "Πώς μπορώ να δω ποιοι άλλοι είναι
εγγεγραμμένοι στο μάθημά μου;",
        "expected_topics_en": ["users", "enrolled",
"participants", "classmates", "list"],
        "expected_topics_el": ["χρήστες", "εγγεγραμμένοι",
"συμμετέχοντες", "συμφοιτητές", "λίστα"],
        "difficulty": "MEDIUM",
        "notes": "User listing feature"
    },
    {
        "id": "M8",
        "question_en": "What types of files can I upload to the
platform?",
        "question_el": "Τι τύπους αρχείων μπορώ να ανεβάσω στην
πλατφόρμα;",
        "expected_topics_en": ["file", "format", "upload",
"supported", "types"],
        "expected_topics_el": ["αρχείο", "μορφή", "ανέβασμα",
"υποστηριζόμενοι", "τύποι"],
        "difficulty": "MEDIUM",
        "notes": "File format question"
    },
    {
        "id": "M9",
        "question_en": "How do I set up notifications for course
updates?",
        "question_el": "Πώς ρυθμίζω ειδοποιήσεις για ενημερώσεις
μαθήματος;",
        "expected_topics_en": ["notifications", "alerts",
"updates", "settings", "email"],
        "expected_topics_el": ["ειδοποιήσεις", "ενημερώσεις",
"ρυθμίσεις", "email"],
        "difficulty": "MEDIUM",
        "notes": "Notification settings"
    },
    {
        "id": "M10",
        "question_en": "Can I see feedback on my submitted
assignments?",
        "question_el": "Μπορώ να δω σχόλια στις εργασίες που
υπέβαλα;",
        "expected_topics_en": ["feedback", "comments",
"assignment", "grade", "review"],
        "expected_topics_el": ["σχόλια", "ανατροφοδότηση",
"εργασία", "βαθμός", "αξιολόγηση"],
        "difficulty": "MEDIUM",
        "notes": "Assignment feedback"
    },
    {
        "id": "M11",
        "question_en": "How do I watch a video lecture?",
        "question_el": "Πώς βλέπω μια βιντεοδιάλεξη;",
        "expected_topics_en": ["video", "lecture", "watch",
"multimedia", "play"],
        "expected_topics_el": ["βίντεο", "διάλεξη",
"παρακολούθηση", "πολυμέσα"],
        "difficulty": "MEDIUM",
        "notes": "Video content access"
    },
    {
        "id": "M12",
        "question_en": "How do I update my profile information?",
        "question_el": "Πώς ενημερώνω τις πληροφορίες του προφίλ
μου;",
        "expected_topics_en": ["profile", "update", "edit",
"personal", "information"],
        "expected_topics_el": ["προφίλ", "ενημέρωση",
"επεξεργασία", "προσωπικά", "πληροφορίες"],
        "difficulty": "MEDIUM",
        "notes": "Profile management"
    },
    {
        "id": "M13",
        "question_en": "How do I join a teleconference session?",
        "question_el": "Πώς συμμετέχω σε μια τηλεδιάσκεψη;",
        "expected_topics_en": ["teleconference", "join",
"video", "meeting", "online"],
        "expected_topics_el": ["τηλεδιάσκεψη", "συμμετοχή",
"βίντεο", "συνάντηση", "διαδικτυακά"],
        "difficulty": "MEDIUM",
        "notes": "Teleconference feature"
    },
    {
        "id": "M14",
        "question_en": "What is a learning path and how do I follow
it?",
        "question_el": "Τι είναι η γραμμή μάθησης και πώς την
ακολουθώ;",
        "expected_topics_en": ["learning path", "progress",
"modules", "sequence", "complete"],
        "expected_topics_el": ["γραμμή μάθησης", "πρόοδος",
"ενότητες", "ακολουθία", "ολοκλήρωση"],
        "difficulty": "MEDIUM",
        "notes": "Learning path feature"
    },
    {
        "id": "M15",
        "question_en": "How do I add an event to the course
calendar?",
        "question_el": "Πώς προσθέτω ένα γεγονός στο ημερολόγιο του
μαθήματος;",
        "expected_topics_en": ["calendar", "event", "add",
"schedule", "date"],
        "expected_topics_el": ["ημερολόγιο", "γεγονός",
"προσθήκη", "πρόγραμμα", "ημερομηνία"],
        "difficulty": "MEDIUM",
        "notes": "Calendar event creation"
    },
]
# VAGUE QUESTIONS (Ambiguous - Tests system's ability to clarify or
make best guess)
# These are intentionally unclear or could have multiple
interpretations
VAGUE_QUESTIONS = [
    {
        "id": "V1",
        "question_en": "Help",
        "question_el": "Βοήθεια",
        "expected_topics_en": ["help", "support", "assistance",
"guide"],
        "expected_topics_el": ["βοήθεια", "υποστήριξη", "οδηγ",
"eclass"],
        "difficulty": "VAGUE",
        "notes": "Single word, very ambiguous"
    },
    {
        "id": "V2",
        "question_en": "It doesn't work",
        "question_el": "Δεν δουλεύει",
        "expected_topics_en": ["problem", "error", "issue",
"support"],
        "expected_topics_el": ["πρόβλημα", "σφάλμα",
"υποστήριξη", "επικοινωνία"],
        "difficulty": "VAGUE",
        "notes": "No context about what doesn't work"
    },
    {
        "id": "V3",
        "question_en": "The thing with the files",
        "question_el": "Αυτό με τα αρχεία",
        "expected_topics_en": ["documents", "files", "upload",
"download"],
        "expected_topics_el": ["έγγραφα", "αρχεία", "ανέβασμα",
"κατέβασμα"],
        "difficulty": "VAGUE",
        "notes": "Vague reference to documents/files"
    },
    {
        "id": "V4",
        "question_en": "How do I do the course stuff?",
        "question_el": "Πώς κάνω τα πράγματα του μαθήματος;",
        "expected_topics_en": ["course", "enroll",
"participate", "access"],
        "expected_topics_el": ["μάθημα", "εγγραφή",
"συμμετοχή", "πρόσβαση"],
        "difficulty": "VAGUE",
        "notes": "Unclear what 'stuff' refers to"
    },
    {
        "id": "V5",
        "question_en": "Where is everything?",
        "question_el": "Πού είναι όλα;",
        "expected_topics_en": ["navigation", "menu",
"portfolio", "interface"],
        "expected_topics_el": ["πλοήγηση", "μενού",
"portfolio", "διεπαφή"],
        "difficulty": "VAGUE",
        "notes": "Extremely vague location question"
    },
    {
        "id": "V6",
        "question_en": "Can you explain?",
        "question_el": "Μπορείς να εξηγήσεις;",
        "expected_topics_en": ["explain", "help",
"information", "guide"],
        "expected_topics_el": ["εξήγηση", "βοήθεια",
"πληροφορίες", "οδηγός"],
        "difficulty": "VAGUE",
        "notes": "No context what to explain"
    },
    {
        "id": "V7",
        "question_en": "The button",
        "question_el": "Το κουμπί",
        "expected_topics_en": ["button", "click", "interface",
"action"],
        "expected_topics_el": ["κουμπί", "κλικ", "διεπαφή",
"ενέργεια"],
        "difficulty": "VAGUE",
        "notes": "Which button?"
    },
    {
        "id": "V8",
        "question_en": "Something about the teacher",
        "question_el": "Κάτι για τον καθηγητή",
        "expected_topics_en": ["teacher", "instructor",
"professor", "contact"],
        "expected_topics_el": ["καθηγητής", "εκπαιδευτής",
"επαφή", "επικοινωνία"],
        "difficulty": "VAGUE",
        "notes": "Vague teacher reference"
    },
    {
        "id": "V9",
        "question_en": "I need to do that thing",
        "question_el": "Πρέπει να κάνω αυτό το πράγμα",
        "expected_topics_en": ["task", "action", "help",
"guide"],
        "expected_topics_el": ["εργασία", "ενέργεια",
"βοήθεια", "οδηγός"],
        "difficulty": "VAGUE",
        "notes": "Extremely vague request"
    },
    {
        "id": "V10",
        "question_en": "Problem with my account",
        "question_el": "Πρόβλημα με τον λογαριασμό μου",
        "expected_topics_en": ["account", "problem", "login",
"password", "support"],
        "expected_topics_el": ["λογαριασμός", "πρόβλημα",
"σύνδεση", "κωδικός", "υποστήριξη"],
        "difficulty": "VAGUE",
        "notes": "Unspecified account problem"
    },
    {
        "id": "V11",
        "question_en": "The video thing",
        "question_el": "Αυτό με το βίντεο",
        "expected_topics_en": ["video", "multimedia", "watch",
"play"],
        "expected_topics_el": ["βίντεο", "πολυμέσα",
"παρακολούθηση"],
        "difficulty": "VAGUE",
        "notes": "Vague video reference"
    },
    {
        "id": "V12",
        "question_en": "What about deadlines?",
        "question_el": "Τι γίνεται με τις προθεσμίες;",
        "expected_topics_en": ["deadline", "assignment",
"date", "submit"],
        "expected_topics_el": ["προθεσμία", "εργασία",
"ημερομηνία", "υποβολή"],
        "difficulty": "VAGUE",
        "notes": "Vague deadline question"
    },
    {
        "id": "V13",
        "question_en": "How does it work?",
        "question_el": "Πώς λειτουργεί;",
        "expected_topics_en": ["work", "function", "use",
"guide"],
        "expected_topics_el": ["λειτουργία", "χρήση",
"οδηγός"],
        "difficulty": "VAGUE",
        "notes": "No context what 'it' is"
    },
    {
        "id": "V14",
        "question_en": "Can I change it?",
        "question_el": "Μπορώ να το αλλάξω;",
        "expected_topics_en": ["change", "edit", "modify",
"update"],
        "expected_topics_el": ["αλλαγή", "επεξεργασία",
"τροποποίηση", "ενημέρωση"],
        "difficulty": "VAGUE",
        "notes": "Unknown what to change"
    },
    {
        "id": "V15",
        "question_en": "Need access",
        "question_el": "Χρειάζομαι πρόσβαση",
        "expected_topics_en": ["access", "permission", "login",
"enroll"],
        "expected_topics_el": ["πρόσβαση", "άδεια", "σύνδεση",
"εγγραφή"],
        "difficulty": "VAGUE",
        "notes": "Unspecified access request"
    },
]
# HARD QUESTIONS (Complex - May not have direct answers)
# These test edge cases, complex scenarios, or questions outside the
knowledge base
HARD_QUESTIONS = [
    {
        "id": "H1",
        "question_en": "Can I submit an assignment after the deadline
if my internet was down?",
        "question_el": "Μπορώ να υποβάλω εργασία μετά την προθεσμία
αν έπεσε το internet μου;",
        "expected_topics_en": ["deadline", "late",
"submission", "extension"],
        "expected_topics_el": ["προθεσμία", "καθυστέρηση",
"υποβολή", "παράταση"],
        "difficulty": "HARD",
        "notes": "Conditional scenario not directly in FAQ"
    },
    {
        "id": "H2",
        "question_en": "How do I integrate external tools like Zoom
or Google Meet with my course?",
        "question_el": "Πώς ενσωματώνω εξωτερικά εργαλεία όπως Zoom ή
Google Meet στο μάθημά μου;",
        "expected_topics_en": ["integration", "external",
"video", "conference"],
        "expected_topics_el": ["ενσωμάτωση", "εξωτερικ",
"βίντεο", "τηλεδιάσκεψη", "zoom"],
        "difficulty": "HARD",
        "notes": "Specific technical integration question"
    },
    {
        "id": "H3",
        "question_en": "What accessibility features are available for
visually impaired students?",
        "question_el": "Ποιες λειτουργίες προσβασιμότητας υπάρχουν
για φοιτητές με προβλήματα όρασης;",
        "expected_topics_en": ["accessibility", "screen reader",
"impaired", "support"],
        "expected_topics_el": ["προσβασιμότητα", "αναγνώστη",
"όραση", "υποστήριξη"],
        "difficulty": "HARD",
        "notes": "Specialized accessibility question"
    },
    {
        "id": "H4",
        "question_en": "How can I export all my course data before
the semester ends?",
        "question_el": "Πώς μπορώ να εξάγω όλα τα δεδομένα του
μαθήματός μου πριν τελειώσει το εξάμηνο;",
        "expected_topics_en": ["export", "backup", "data",
"download"],
        "expected_topics_el": ["εξαγωγή", "αντίγραφο",
"δεδομένα", "κατέβασμα"],
        "difficulty": "HARD",
        "notes": "Data management question"
    },
    {
        "id": "H5",
        "question_en": "My assignment shows 85% similarity on
Turnitin but I didn't copy - what can I do?",
        "question_el": "Η εργασία μου δείχνει 85% ομοιότητα στο
Turnitin αλλά δεν αντέγραψα - τι μπορώ να κάνω;",
        "expected_topics_en": ["turnitin", "similarity",
"plagiarism", "appeal"],
        "expected_topics_el": ["turnitin", "ομοιότητα",
"λογοκλοπή", "ένσταση"],
        "difficulty": "HARD",
        "notes": "Complex problem-solving scenario"
    },
    {
        "id": "H6",
        "question_en": "Can multiple instructors manage the same
course simultaneously?",
        "question_el": "Μπορούν πολλοί εκπαιδευτές να διαχειρίζονται
το ίδιο μάθημα ταυτόχρονα;",
        "expected_topics_en": ["instructor", "multiple",
"manage", "collaborate", "course"],
        "expected_topics_el": ["εκπαιδευτής", "πολλοί",
"διαχείριση", "συνεργασία", "μάθημα"],
        "difficulty": "HARD",
        "notes": "Multi-instructor scenario"
    },
    {
        "id": "H7",
        "question_en": "How do I set up automated grading for
multiple choice quizzes?",
        "question_el": "Πώς ρυθμίζω αυτόματη βαθμολόγηση για τεστ
πολλαπλής επιλογής;",
        "expected_topics_en": ["grading", "automatic", "quiz",
"multiple choice", "score"],
        "expected_topics_el": ["βαθμολόγηση", "αυτόματη",
"τεστ", "πολλαπλής επιλογής", "σκορ"],
        "difficulty": "HARD",
        "notes": "Auto-grading setup"
    },
    {
        "id": "H8",
        "question_en": "Is there an API to integrate eClass with our
university's student information system?",
        "question_el": "Υπάρχει API για ενσωμάτωση του eClass με το
σύστημα πληροφοριών φοιτητών του πανεπιστημίου μας;",
        "expected_topics_en": ["API", "integration", "system",
"data", "external"],
        "expected_topics_el": ["API", "ενσωμάτωση", "σύστημα",
"δεδομένα", "εξωτερικό"],
        "difficulty": "HARD",
        "notes": "Technical API question"
    },
    {
        "id": "H9",
        "question_en": "How can I restore a deleted course that was
accidentally removed?",
        "question_el": "Πώς μπορώ να επαναφέρω ένα μάθημα που
διαγράφηκε κατά λάθος;",
        "expected_topics_en": ["restore", "deleted", "recover",
"course", "backup"],
        "expected_topics_el": ["επαναφορά", "διαγραμμένο",
"ανάκτηση", "μάθημα", "αντίγραφο"],
        "difficulty": "HARD",
        "notes": "Data recovery scenario"
    },
    {
        "id": "H10",
        "question_en": "What happens to my course content if my
instructor account expires?",
        "question_el": "Τι γίνεται με το περιεχόμενο του μαθήματός
μου αν λήξει ο λογαριασμός εκπαιδευτή;",
        "expected_topics_en": ["account", "expire", "content",
"data", "access"],
        "expected_topics_el": ["λογαριασμός", "λήξη",
"περιεχόμενο", "δεδομένα", "πρόσβαση"],
        "difficulty": "HARD",
        "notes": "Account expiration scenario"
    },
    {
        "id": "H11",
        "question_en": "Can I set different deadlines for different
student groups in the same assignment?",
        "question_el": "Μπορώ να ορίσω διαφορετικές προθεσμίες για
διαφορετικές ομάδες φοιτητών στην ίδια εργασία;",
        "expected_topics_en": ["deadline", "groups",
"assignment", "different", "students"],
        "expected_topics_el": ["προθεσμία", "ομάδες",
"εργασία", "διαφορετικές", "φοιτητές"],
        "difficulty": "HARD",
        "notes": "Group-specific deadlines"
    },
    {
        "id": "H12",
        "question_en": "How do I configure SSO (Single Sign-On) for
my institution?",
        "question_el": "Πώς ρυθμίζω SSO (Single Sign-On) για το
ίδρυμά μου;",
        "expected_topics_en": ["SSO", "login",
"authentication", "institution", "configure"],
        "expected_topics_el": ["SSO", "σύνδεση", "ταυτοποίηση",
"ίδρυμα", "ρύθμιση"],
        "difficulty": "HARD",
        "notes": "Enterprise SSO configuration"
    },
    {
        "id": "H13",
        "question_en": "Is there a mobile app and does it support
offline access to course materials?",
        "question_el": "Υπάρχει εφαρμογή κινητού και υποστηρίζει
πρόσβαση εκτός σύνδεσης στο υλικό μαθήματος;",
        "expected_topics_en": ["mobile", "app", "offline",
"access", "download"],
        "expected_topics_el": ["κινητό", "εφαρμογή", "εκτός
σύνδεσης", "πρόσβαση", "κατέβασμα"],
        "difficulty": "HARD",
        "notes": "Mobile app capabilities"
    },
    {
        "id": "H14",
        "question_en": "How can I track student engagement and time
spent on course materials?",
        "question_el": "Πώς μπορώ να παρακολουθήσω τη συμμετοχή
φοιτητών και τον χρόνο που αφιερώνουν στο υλικό;",
        "expected_topics_en": ["analytics", "engagement",
"tracking", "time", "statistics"],
        "expected_topics_el": ["αναλυτικά", "συμμετοχή",
"παρακολούθηση", "χρόνος", "στατιστικά"],
        "difficulty": "HARD",
        "notes": "Learning analytics"
    },
    {
        "id": "H15",
        "question_en": "What security measures protect student data
and comply with GDPR?",
        "question_el": "Ποια μέτρα ασφαλείας προστατεύουν τα δεδομένα
φοιτητών και συμμορφώνονται με το GDPR;",
        "expected_topics_en": ["security", "GDPR", "privacy",
"data", "protection"],
        "expected_topics_el": ["ασφάλεια", "GDPR", "απόρρητο",
"δεδομένα", "προστασία"],
        "difficulty": "HARD",
        "notes": "Security and compliance"
    },
]
# EDGE CASE QUESTIONS (Testing robustness)
EDGE_CASES = [
    {
        "id": "E1",
        "question_en": "asdfghjkl",
        "question_el": "ασδφγηξκλ",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Gibberish input"
    },
    {
        "id": "E2",
        "question_en": "LOGIN LOGIN LOGIN HOW DO I LOGIN???!!!",
        "question_el": "ΣΥΝΔΕΣΗ ΣΥΝΔΕΣΗ ΣΥΝΔΕΣΗ ΠΩΣ ΚΑΝΩ
ΣΥΝΔΕΣΗ???!!!",
        "expected_topics_en": ["login", "sign in", "username",
"password"],
        "expected_topics_el": ["σύνδεση", "είσοδος",
"username", "κωδικό"],
        "difficulty": "EDGE",
        "notes": "Repeated/emphatic query with caps"
    },
    {
        "id": "E3",
        "question_en": "What is the meaning of life?",
        "question_el": "Ποιο είναι το νόημα της ζωής;",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Completely off-topic question"
    },
    {
        "id": "E4",
        "question_en": "",
        "question_el": "",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Empty input"
    },
    {
        "id": "E5",
        "question_en": "How to hack the system and change my
grades?",
        "question_el": "Πώς να χακάρω το σύστημα και να αλλάξω τους
βαθμούς μου;",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Inappropriate/malicious query"
    },
    {
        "id": "E6",
        "question_en": "🎉🎊🎈 How do I party? 🎉🎊🎈",
        "question_el": "🎉🎊🎈 Πώς κάνω πάρτι; 🎉🎊🎈",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Emoji-heavy off-topic"
    },
    {
        "id": "E7",
        "question_en": "SELECT * FROM users WHERE 1=1; DROP TABLE
users;--",
        "question_el": "SELECT * FROM users WHERE 1=1; DROP TABLE
users;--",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "SQL injection attempt"
    },
    {
        "id": "E8",
        "question_en": "<script>alert('XSS')</script>",
        "question_el": "<script>alert('XSS')</script>",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "XSS injection attempt"
    },
    {
        "id": "E9",
        "question_en": "                    ",
        "question_el": "                    ",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Whitespace-only input"
    },
    {
        "id": "E10",
        "question_en": "a",
        "question_el": "α",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Single character input"
    },
    {
        "id": "E11",
        "question_en": "Can you write me an essay about climate
change for my biology class?",
        "question_el": "Μπορείς να μου γράψεις μια έκθεση για την
κλιματική αλλαγή για το μάθημα βιολογίας;",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Academic dishonesty request"
    },
    {
        "id": "E12",
        "question_en": "What is the weather today?",
        "question_el": "Τι καιρό κάνει σήμερα;",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Off-topic general question"
    },
    {
        "id": "E13",
        "question_en": "Tell me a joke",
        "question_el": "Πες μου ένα ανέκδοτο",
        "expected_topics_en": [],
        "expected_topics_el": [],
        "difficulty": "EDGE",
        "notes": "Entertainment request"
    },
    {
        "id": "E14",
        "question_en": "password password password username admin
admin root",
        "question_el": "κωδικός κωδικός κωδικός username admin admin
root",
        "expected_topics_en": ["password", "username"],
        "expected_topics_el": ["κωδικός", "username"],
        "difficulty": "EDGE",
        "notes": "Keyword stuffing"
    },
    {
        "id": "E15",
        "question_en": "Hello! How are you? Nice to meet you! What's
your name?",
        "question_el": "Γεια σου! Τι κάνεις; Χάρηκα! Πώς σε λένε;",
        "expected_topics_en": ["hello", "help"],
        "expected_topics_el": ["γεια", "βοήθεια"],
        "difficulty": "EDGE",
        "notes": "Social chit-chat"
    },
]
# GREEKLISH QUESTIONS (Greek content written with Latin alphabet)
# Testing cross-lingual performance with Greeklish variants
GREEKLISH_QUESTIONS = {
    "BASIC": [
        {
            "id": "GL_B1",
            "question": "Pos kano syndesi?",
            "expected_topics": ["syndesi", "login", "username",
"password", "kodikos"],
            "difficulty": "BASIC",
            "notes": "Greeklish: How do I log in?"
        },
        {
            "id": "GL_B2",
            "question": "Pos dimioyrgo logarjasmo fotiti?",
            "expected_topics": ["fotitis", "logarjasmos",
"eggrafi", "dimioyrgia"],
            "difficulty": "BASIC",
            "notes": "Greeklish: How do I create a student account?"
        },
        {
            "id": "GL_B3",
            "question": "Ti ine to portfolio?",
            "expected_topics": ["portfolio", "mathimata",
"arxiki", "selida"],
            "difficulty": "BASIC",
            "notes": "Greeklish: What is the portfolio?"
        },
        {
            "id": "GL_B4",
            "question": "Pos ypovalo mia ergasia?",
            "expected_topics": ["ergasia", "ypovoli",
"anevasma", "prothesmia"],
            "difficulty": "BASIC",
            "notes": "Greeklish: How do I submit an assignment?"
        },
        {
            "id": "GL_B5",
            "question": "Pou boro na vro ta mathimata mou?",
            "expected_topics": ["mathimata", "lista",
"eggegramenos"],
            "difficulty": "BASIC",
            "notes": "Greeklish: Where can I find my courses?"
        },
        {
            "id": "GL_B6",
            "question": "Pos eggrafome se ena mathima?",
            "expected_topics": ["eggrafi", "mathima",
"symmetoxi"],
            "difficulty": "BASIC",
            "notes": "Greeklish: How do I enroll in a course?"
        },
    ],
    "MEDIUM": [
        {
            "id": "GL_M1",
            "question": "Pos boro na allakso tin anartimeni ergasia
mou meta tin ypovoli?",
            "expected_topics": ["eggrafi", "allagi", "ypovoli",
"anartimeni"],
            "difficulty": "MEDIUM",
            "notes": "Greeklish: How can I change my uploaded
assignment after submission?"
        },
        {
            "id": "GL_M2",
            "question": "Ti typos arxeion ypostirizete gia tin
ypovoli ergasion?",
            "expected_topics": ["arxeia", "typos", "ypovoli",
"format"],
            "difficulty": "MEDIUM",
            "notes": "Greeklish: What file types are supported for
assignment submission?"
        },
        {
            "id": "GL_M3",
            "question": "Pos boro na epistrepso se proigoumeni ekdosi
tis ergasias mou?",
            "expected_topics": ["ekdosi", "epistrofi",
"istoriko", "ergasia"],
            "difficulty": "MEDIUM",
            "notes": "Greeklish: How can I revert to a previous
version of my assignment?"
        },
        {
            "id": "GL_M4",
            "question": "Yparchei periorymos megethous arxeiou gia
anevasma?",
            "expected_topics": ["megethos", "periorymos",
"arxeio", "anevasma"],
            "difficulty": "MEDIUM",
            "notes": "Greeklish: Is there a file size limit for
uploads?"
        },
        {
            "id": "GL_M5",
            "question": "Pos boro na vlepo tous vathmous mou se ola
ta mathimata?",
            "expected_topics": ["vathmoi", "mathimata",
"apotelesmata"],
            "difficulty": "MEDIUM",
            "notes": "Greeklish: How can I see my grades across all
courses?"
        },
    ],
    "VAGUE": [
        {
            "id": "GL_V1",
            "question": "Den doulevei kati",
            "expected_topics": ["provlima", "voitheia",
"yprostiriji"],
            "difficulty": "VAGUE",
            "notes": "Greeklish: Something doesn't work"
        },
        {
            "id": "GL_V2",
            "question": "Exo provlima me to mathima",
            "expected_topics": ["provlima", "mathima",
"voitheia"],
            "difficulty": "VAGUE",
            "notes": "Greeklish: I have a problem with the course"
        },
        {
            "id": "GL_V3",
            "question": "Pos kano afto to pragma?",
            "expected_topics": ["voitheia", "odigies"],
            "difficulty": "VAGUE",
            "notes": "Greeklish: How do I do that thing?"
        },
        {
            "id": "GL_V4",
            "question": "Ti prepei na kano meta?",
            "expected_topics": ["epomena vimata", "odigies"],
            "difficulty": "VAGUE",
            "notes": "Greeklish: What should I do next?"
        },
        {
            "id": "GL_V5",
            "question": "Pou ine to koympi?",
            "expected_topics": ["interface", "navigation"],
            "difficulty": "VAGUE",
            "notes": "Greeklish: Where is the button?"
        },
    ],
    "HARD": [
        {
            "id": "GL_H1",
            "question": "Pos boro na rythmiso tin prosvasimotita
mathimatos monon se sigkekrimenes imeres?",
            "expected_topics": ["prosvasimotita", "imerominia",
"rythmiseis"],
            "difficulty": "HARD",
            "notes": "Greeklish: How can I configure course
accessibility only on specific dates?"
        },
        {
            "id": "GL_H2",
            "question": "Yparchei api gia diachirisi mathimaton kai
foititon programmatistika?",
            "expected_topics": ["api", "programmatismos",
"diachirisi"],
            "difficulty": "HARD",
            "notes": "Greeklish: Is there an API for programmatic
course and student management?"
        },
        {
            "id": "GL_H3",
            "question": "Pos ypologizontai oi telikes vathmologies
otan yparxoun pola ktitiria axiologisis?",
            "expected_topics": ["vathmologia", "ypologismos",
"axiologisi"],
            "difficulty": "HARD",
            "notes": "Greeklish: How are final grades calculated with
multiple assessment criteria?"
        },
        {
            "id": "GL_H4",
            "question": "Borite na eksigisete tin diafora metaksy
synchronous kai asynchronous mathimaton?",
            "expected_topics": ["synchronous", "asynchronous",
"mathimata"],
            "difficulty": "HARD",
            "notes": "Greeklish: Can you explain the difference
between synchronous and asynchronous courses?"
        },
        {
            "id": "GL_H5",
            "question": "Poia metra asfaleias prostatevoun ta
dedomena foititon kai symmorfononte me to GDPR?",
            "expected_topics": ["asfaleia", "GDPR", "dedomena",
"prostasia"],
            "difficulty": "HARD",
            "notes": "Greeklish: What security measures protect
student data and comply with GDPR?"
        },
    ],
    "EDGE": [
        {
            "id": "GL_E1",
            "question": "asdfghjklqwerty",
            "expected_topics": [],
            "difficulty": "EDGE",
            "notes": "Greeklish: Gibberish input"
        },
        {
            "id": "GL_E2",
            "question": "SYNDESI SYNDESI POS KANO SYNDESI???!!!",
            "expected_topics": ["syndesi", "login"],
            "difficulty": "EDGE",
            "notes": "Greeklish: Repeated/emphatic login query"
        },
        {
            "id": "GL_E3",
            "question": "Pio ine to noima tis zois?",
            "expected_topics": [],
            "difficulty": "EDGE",
            "notes": "Greeklish: Meaning of life - off topic"
        },
        {
            "id": "GL_E4",
            "question": "",
            "expected_topics": [],
            "difficulty": "EDGE",
            "notes": "Empty input"
        },
        {
            "id": "GL_E5",
            "question": "Pos na xakarο to systima kai na allakso tous
vathmous mou?",
            "expected_topics": [],
            "difficulty": "EDGE",
            "notes": "Greeklish: Inappropriate hacking query"
        },
    ]
}
#============================================================================
# EVALUATION FUNCTIONS
#============================================================================
def evaluate_response(question_data: Dict, response: str, language: str
= 'en') -> Dict:
    """
    Evaluate the quality of a RAG response.
   
    Returns a dictionary with evaluation metrics.
    """
    # Handle different question formats (Greeklish vs en/el)
    if language == 'greeklish':
        question = question_data['question']
        expected_topics = question_data['expected_topics']
    else:
        question = question_data[f'question_{language}']
        # Get language-specific expected topics
        topics_key = f'expected_topics_{language}'
        if topics_key in question_data:
            expected_topics = question_data[topics_key]
        else:
            # Fallback to old format for backwards compatibility
            expected_topics = question_data.get('expected_topics',
[])
   
    # Check if response contains expected topics
    response_lower = response.lower()
    topics_found = [topic for topic in expected_topics if topic.lower()
in response_lower]
    topic_coverage = len(topics_found) / len(expected_topics) if
expected_topics else 0
   
    # Determine response type from emoji
    if response.startswith("📄"):
        response_type = "RAG (Document)"
    elif response.startswith("❓"):
        response_type = "FAQ"
    elif response.startswith("🤖"):
        response_type = "AI Generated"
    else:
        response_type = "Fallback"
   
    # Check response quality indicators
    has_source_citation = "📚" in response or "Sources:" in response
or "Πηγές:" in response
    has_actionable_steps = any(marker in response for marker in
["1.", "1)", "•", "Step", "Βήμα"])
    response_length = len(response)
   
    # Simple relevance score based on topic coverage and response
characteristics
    relevance_score = topic_coverage * 0.6  # 60% weight on topic
coverage
    if has_actionable_steps:
        relevance_score += 0.2
    if response_type in ["RAG (Document)", "FAQ"]:
        relevance_score += 0.2
    elif response_type == "AI Generated":
        relevance_score += 0.1
   
    relevance_score = min(relevance_score, 1.0)  # Cap at 1.0
   
    return {
        "question_id": question_data["id"],
        "difficulty": question_data["difficulty"],
        "question": question,
        "response_type": response_type,
        "topics_found": topics_found,
        "topic_coverage": f"{topic_coverage:.0%}",
        "relevance_score": f"{relevance_score:.0%}",
        "has_citations": has_source_citation,
        "has_steps": has_actionable_steps,
        "response_length": response_length,
        "response_preview": response[:200] + "..." if
len(response) > 200 else response
    }
def run_test_suite(language: str = 'en', verbose: bool = True,
show_responses: bool = False) -> Dict:
    """
    Run the complete test suite and return results.
   
    Args:
        language: 'en', 'el', or 'greeklish'
        verbose: Show progress and status
        show_responses: Print full LLM response content for verification
    """
    # Handle Greeklish separately since it has different structure
    if language == 'greeklish':
        all_questions = GREEKLISH_QUESTIONS
    else:
        all_questions = {
            "BASIC": BASIC_QUESTIONS,
            "MEDIUM": MEDIUM_QUESTIONS,
            "VAGUE": VAGUE_QUESTIONS,
            "HARD": HARD_QUESTIONS,
            "EDGE": EDGE_CASES
        }
   
    results = {
        "timestamp": datetime.now().isoformat(),
        "language": language,
        "config": {
            "query_expansion": USE_QUERY_EXPANSION,
            "reranking": USE_RERANKING,
            "doc_threshold": DOCUMENT_CONFIDENCE_THRESHOLD,
            "faq_threshold": FAQ_CONFIDENCE_THRESHOLD
        },
        "summary": {},
        "details": []
    }
   
    total_tests = 0
    total_relevant = 0
    category_scores = {}
   
    print(f"\n{'='*70}")
    print(f"🧪 RAG ACCURACY EVALUATION - Language:
{language.upper()}")
    print(f"{'='*70}\n")
   
    for category, questions in all_questions.items():
        if verbose:
            print(f"\n📋 Testing {category} Questions
({len(questions)} tests)")
            print("-" * 50)
       
        category_results = []
        category_relevant = 0
       
        for q_data in questions:
            # Handle different question formats (Greeklish vs en/el)
            if language == 'greeklish':
                question = q_data['question']
                expected_topics = q_data['expected_topics']
            else:
                question = q_data[f'question_{language}']
                expected_topics =
q_data[f'expected_topics_{language}']
           
            # Skip empty questions
            if not question.strip():
                if verbose:
                    print(f"  [{q_data['id']}] ⏭️  Skipped (empty
input)")
                continue
           
            # Time the response
            start_time = time.time()
            response = get_rag_response(question, language)
            elapsed_time = time.time() - start_time
           
            # Evaluate the response
            evaluation = evaluate_response(q_data, response, language)
            evaluation["response_time"] = f"{elapsed_time:.2f}s"
            evaluation["full_response"] = response
           
            category_results.append(evaluation)
           
            # Count as relevant if relevance score >= 50%
            relevance_pct =
float(evaluation["relevance_score"].strip('%')) / 100
            if relevance_pct >= 0.5:
                category_relevant += 1
                total_relevant += 1
           
            total_tests += 1
           
            if verbose:
                status = "✅" if relevance_pct >= 0.5 else "⚠️" if
relevance_pct >= 0.3 else "❌"
                print(f"  [{q_data['id']}] {status}
{evaluation['response_type']:15} \| "
                      f"Relevance:
{evaluation['relevance_score']:>4} \| "
                      f"Topics: {evaluation['topic_coverage']:>4}
\| "
                      f"Time: {evaluation['response_time']}")
               
                # Show full response content if requested (for
verification)
                if show_responses:
                    print(f"\n  {'─'*60}")
                    print(f"  📝 QUERY: {question[:100]}{'...' if
len(question) > 100 else ''}")
                    print(f"  {'─'*60}")
                    print(f"  📄 RESPONSE:")
                    # Show first 15 lines of response
                    response_lines = response.split('\n')[:15]
                    for line in response_lines:
                        print(f"     {line[:120]}")
                    if len(response.split('\n')) > 15:
                        print(f"     ...
({len(response.split(chr(10)))} total lines)")
                    print(f"  {'─'*60}\n")
       
        # Calculate category accuracy
        if language == 'greeklish':
            non_empty_questions = [q for q in questions if
q['question'].strip()]
        else:
            non_empty_questions = [q for q in questions if
q[f'question_{language}'].strip()]
        category_accuracy = category_relevant / len(non_empty_questions)
if non_empty_questions else 0
        category_scores[category] = category_accuracy
       
        results["details"].extend(category_results)
       
        if verbose:
            print(f"\n  📊 {category} Accuracy:
{category_accuracy:.0%} ({category_relevant}/{len(category_results)})")
   
    # Calculate overall summary
    overall_accuracy = total_relevant / total_tests if total_tests > 0
else 0
   
    results["summary"] = {
        "total_tests": total_tests,
        "total_relevant": total_relevant,
        "overall_accuracy": f"{overall_accuracy:.0%}",
        "category_scores": {k: f"{v:.0%}" for k, v in
category_scores.items()}
    }
   
    # Print final summary
    print(f"\n{'='*70}")
    print("📊 FINAL RESULTS SUMMARY")
    print(f"{'='*70}")
    print(f"\n  Overall Accuracy: {overall_accuracy:.0%}
({total_relevant}/{total_tests} relevant responses)")
    print(f"\n  By Category:")
    for category, score in category_scores.items():
        bar = "█" * int(score * 20) + "░" * (20 - int(score *
20))
        print(f"    {category:8} [{bar}] {score:.0%}")
   
    print(f"\n  Configuration:")
    print(f"    • Query Expansion: {'✅' if USE_QUERY_EXPANSION else
'❌'}")
    print(f"    • Re-ranking: {'✅' if USE_RERANKING else '❌'}")
    print(f"    • Document Threshold:
{DOCUMENT_CONFIDENCE_THRESHOLD}")
    print(f"    • FAQ Threshold: {FAQ_CONFIDENCE_THRESHOLD}")
    print(f"\n{'='*70}\n")
   
    return results
def run_single_test(question: str, language: str = 'en') -> None:
    """
    Run a single test query and display detailed results.
    """
    print(f"\n{'='*70}")
    print(f"🔬 SINGLE QUERY TEST")
    print(f"{'='*70}")
    print(f"\n📝 Question: {question}")
    print(f"🌐 Language: {language}")
   
    # Show preprocessing
    processed = preprocess_query(question)
    print(f"🔄 Preprocessed: {processed}")
   
    if USE_QUERY_EXPANSION:
        expansions = expand_query(question, language)
        print(f"📈 Query Expansions: {expansions}")
   
    # Get response
    print(f"\n⏳ Getting response...")
    start_time = time.time()
    response = get_rag_response(question, language)
    elapsed_time = time.time() - start_time
   
    print(f"\n{'─'*70}")
    print(f"📤 RESPONSE ({elapsed_time:.2f}s):")
    print(f"{'─'*70}")
    print(response)
    print(f"{'─'*70}\n")
def compare_with_without_enhancements(question: str, language: str =
'en') -> None:
    """
    Compare response quality with and without accuracy enhancements.
    """
    global USE_QUERY_EXPANSION, USE_RERANKING
   
    print(f"\n{'='*70}")
    print(f"⚖️  COMPARISON: With vs Without Enhancements")
    print(f"{'='*70}")
    print(f"📝 Question: {question}\n")
   
    # Test WITH enhancements
    USE_QUERY_EXPANSION = True
    USE_RERANKING = True
   
    print("🔹 WITH Query Expansion + Re-ranking:")
    start = time.time()
    response_with = get_rag_response(question, language)
    time_with = time.time() - start
    print(f"   Time: {time_with:.2f}s")
    print(f"   Response: {response_with[:300]}...")
   
    # Test WITHOUT enhancements
    USE_QUERY_EXPANSION = False
    USE_RERANKING = False
   
    print("\n🔸 WITHOUT Query Expansion + Re-ranking:")
    start = time.time()
    response_without = get_rag_response(question, language)
    time_without = time.time() - start
    print(f"   Time: {time_without:.2f}s")
    print(f"   Response: {response_without[:300]}...")
   
    # Reset to default
    USE_QUERY_EXPANSION = True
    USE_RERANKING = True
   
    print(f"\n📊 Time difference: {(time_with -
time_without)*1000:.0f}ms")
    print(f"{'='*70}\n")
#============================================================================
# MAIN EXECUTION
#============================================================================
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧪 RAG ACCURACY EVALUATION SUITE")
    print("="*70)
    print("\nOptions:")
    print("  1. Run full test suite (English)")
    print("  2. Run full test suite (Greek)")
    print("  3. Run full test suite (Greeklish)")
    print("  4. Run single query test")
    print("  5. Compare with/without enhancements")
    print("  6. Run all languages")
    print("  7. Run all languages with full response output")
    print("  0. Exit")
   
    while True:
        try:
            choice = input("\nSelect option (0-7): ").strip()
           
            if choice == "0":
                print("👋 Goodbye!")
                break
            elif choice == "1":
                results = run_test_suite(language='en', verbose=True,
show_responses=True)
            elif choice == "2":
                results = run_test_suite(language='el', verbose=True,
show_responses=True)
            elif choice == "3":
                results = run_test_suite(language='greeklish',
verbose=True, show_responses=True)
            elif choice == "4":
                question = input("Enter your question: ").strip()
                lang = input("Language (en/el/greeklish) [en]:
").strip() or 'en'
                run_single_test(question, lang)
            elif choice == "5":
                question = input("Enter your question: ").strip()
                lang = input("Language (en/el/greeklish) [en]:
").strip() or 'en'
                compare_with_without_enhancements(question, lang)
            elif choice == "6":
                print("\n" + "="*70)
                print("📊 RUNNING ALL LANGUAGES")
                print("="*70)
                results_en = run_test_suite(language='en',
verbose=True, show_responses=True)
                results_el = run_test_suite(language='el',
verbose=True, show_responses=True)
                results_greeklish =
run_test_suite(language='greeklish', verbose=True,
show_responses=True)
            elif choice == "7":
                print("\n" + "="*70)
                print("📊 RUNNING ALL LANGUAGES WITH FULL RESPONSE
OUTPUT")
                print("="*70)
                results_en = run_test_suite(language='en',
verbose=True, show_responses=True)
                results_el = run_test_suite(language='el',
verbose=True, show_responses=True)
                results_greeklish =
run_test_suite(language='greeklish', verbose=True,
show_responses=True)
            else:
                print("Invalid option. Please select 0-7.")
        except KeyboardInterrupt:
            print("\n\n👋 Test interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
