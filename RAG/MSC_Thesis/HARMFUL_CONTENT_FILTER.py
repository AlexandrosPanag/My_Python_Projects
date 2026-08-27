#
╔══════════════════════════════════════════════════════════════════════════════╗
# ║                     HARMFUL CONTENT FILTER DATABASE                
         ║
# ║              Comprehensive profanity and safety filter for RAG    
          ║
#
╠══════════════════════════════════════════════════════════════════════════════╣
# ║  Save this as: harmful_content_filter.py                          
          ║
# ║  Place in same folder as RAG.py                                    
         ║
#
╚══════════════════════════════════════════════════════════════════════════════╝
"""
DETECTION STRATEGY:
- Multi-lingual pattern matching (English & Greek)
- Context-aware detection (not just simple word blocking)
- Severity levels (block vs warn)
- Handles leetspeak, special chars, spacing tricks
"""
import html
import urllib.parse
import re
#
═══════════════════════════════════════════════════════════════════════════════
#                    HTML/URL DECODING (OBFUSCATION DETECTION)
#
═══════════════════════════════════════════════════════════════════════════════
def decode_obfuscated_input(text: str) -> str:
    """
    Decode HTML entities and URL encoding to catch obfuscated harmful
content.
   
    Examples:
        "how do i make b&#111;mbs" → "how do i make bombs"
        "how%20to%20make%20bombs" → "how to make bombs"
        "&lt;script&gt;hack&lt;/script&gt;" →
"<script>hack</script>"
        "b&amp;#111;mb" → "bomb"
    """
    try:
        # Decode HTML entities multiple times (nested encoding)
        decoded = text
        for _ in range(5):  # Max 5 levels of encoding
            temp = html.unescape(decoded)
            # Also decode numeric HTML entities manually (&#111; = o)
            temp = re.sub(r'&#(\d+);', lambda m:
chr(int(m.group(1))), temp)
            temp = re.sub(r'&#x([0-9a-fA-F]+);', lambda m:
chr(int(m.group(1), 16)), temp)
           
            # Decode URL encoding
            try:
                temp = urllib.parse.unquote(temp)
                temp = urllib.parse.unquote_plus(temp)
            except:
                pass
           
            # If no change, we're done
            if temp == decoded:
                break
            decoded = temp
       
        return decoded
    except Exception as e:
        # If decoding fails, return original
        return text
   
   
#
═══════════════════════════════════════════════════════════════════════════════
#                           HARMFUL CONTENT CATEGORIES
#
═══════════════════════════════════════════════════════════════════════════════
HARMFUL_PATTERNS = {
    # ─── VIOLENCE & WEAPONS ───
    'violence': {
        'en': [
            'how to make a bomb', 'make bomb', 'build bomb',
'create bomb',
            'make explosive', 'build explosive', 'create
explosive',
            'how to kill', 'murder someone', 'assassinate',
            'make weapon', 'build weapon', 'create weapon',
            'shoot up', 'mass shooting', 'school shooting',
            'pipe bomb', 'molotov', 'ieds', 'improvised
explosive',
            'poison someone', 'how to hurt', 'attack someone',
            'suicide bomb', 'nail bomb', 'pressure cooker bomb',
            'fertilizer bomb', 'ammonium nitrate', 'anfo
explosive',
            'hurt people', 'harm people', 'injure people',
            'violent attack', 'cause harm'
        ],
        'el': [
            'πως να φτιάξω βόμβα', 'κατασκευή βόμβας', 'φτιάξω
βόμβα',
            'πως να σκοτώσω', 'φόνος', 'δολοφονία',
            'κατασκευή όπλου', 'φτιάξω όπλο',
            'πως να βλάψω', 'πως να πληγώσω',
            'εκρηκτικό', 'κατασκευή εκρηκτικού'
        ]
    },
   
    # ─── ILLEGAL SUBSTANCES ───
    'drugs': {
        'en': [
            'how to make meth', 'cook meth', 'manufacture meth',
            'make drugs', 'synthesize drugs', 'drug recipe',
            'how to grow weed', 'cannabis cultivation',
            'make cocaine', 'make heroin', 'make lsd',
            'drug dealing', 'sell drugs', 'distribute drugs',
            'fentanyl synthesis', 'mdma synthesis',
            'crack cocaine', 'crystal meth recipe'
        ],
        'el': [
            'πως να φτιάξω ναρκωτικά', 'παρασκευή ναρκωτικών',
            'καλλιέργεια χασίς', 'πως να καλλιεργήσω',
            'συνταγή ναρκωτικών'
        ]
    },
   
   
   
    # ─── HACKING & CYBERCRIME ───
    'hacking': {
        'en': [
            'hack into', 'break into system', 'bypass security',
            'crack password', 'password cracking', 'brute force
password',
            'steal data', 'data breach', 'unauthorized access',
            'ddos attack', 'dos attack', 'denial of service',
            'sql injection', 'xss attack', 'cross site scripting',
            'phishing tutorial', 'create phishing', 'fake login
page',
            'keylogger', 'install keylogger', 'remote access
trojan',
            'ransomware', 'create virus', 'malware tutorial',
            'credit card fraud', 'steal credit card', 'card
skimming',
            'identity theft', 'steal identity', 'fake identity',
            'hack wifi', 'crack wifi password', 'wpa crack',
            'exploit vulnerability', 'zero day exploit'
        ],
        'el': [
            'χακάρισμα', 'πως να χακάρω', 'σπάσιμο κωδικού',
            'κλοπή δεδομένων', 'παράκαμψη ασφάλειας',
            'επίθεση ddos', 'κλοπή πιστωτικής',
            'ψεύτικη ταυτότητα', 'κλοπή ταυτότητας'
        ]
    },
   
    # ─── ACADEMIC DISHONESTY ───
    'cheating': {
        'en': [
            'cheat on exam', 'exam cheating', 'test cheating',
            'answer key', 'steal answers', 'copy answers',
            'write my essay', 'do my homework', 'complete my
assignment',
            'plagiarize', 'plagiarism tool', 'essay mill',
            'fake diploma', 'fake degree', 'fake certificate',
            'change my grade', 'hack grades', 'alter grades',
            'bypass plagiarism', 'avoid turnitin', 'cheat
turnitin',
            'exam answers', 'test bank', 'answer sheet'
        ],
        'el': [
            'πως να κλέψω στις εξετάσεις', 'αντιγραφή εξετάσεων',
            'αλλαγή βαθμού', 'χακάρισμα βαθμών',
            'κλοπή απαντήσεων', 'κάνε την εργασία μου',
            'πλαγιατισμός', 'αποφυγή antiplagio'
        ]
    },
   
    # ─── EXPLICIT CONTENT ───
    'explicit': {
        'en': [
            'child porn', 'child sexual', 'csam', 'child abuse
material',
            'underage', 'minor sexual', 'pedo', 'pedophile',
            'sex with minor', 'groom child', 'sexual abuse child',
            'revenge porn', 'non consensual', 'deepfake porn',
            'hidden camera', 'spy camera', 'upskirt', 'voyeur'
        ],
        'el': [
            'παιδική πορνογραφία', 'σεξουαλική κακοποίηση ανηλίκου',
            'ανήλικος', 'πορνό εκδίκησης'
        ]
    },
   
    # ─── SELF-HARM ───
    'self_harm': {
        'en': [
            'how to suicide', 'kill myself', 'end my life',
            'suicide method', 'painless suicide', 'ways to die',
            'overdose on', 'lethal dose', 'fatal dose',
            'hanging method', 'suffocation method',
            'self harm', 'cut myself', 'hurt myself',
            'suicide tutorial', 'commit suicide'
        ],
        'el': [
            'πως να αυτοκτονήσω', 'να σκοτώσω τον εαυτό μου',
            'τρόποι θανάτου', 'μέθοδοι αυτοκτονίας',
            'αυτοτραυματισμός'
        ]
    },
   
    # ─── DISCRIMINATION & HATE ───
    'hate_speech': {
        'en': [
            'hate speech', 'racist slur', 'racial slur',
            'how to discriminate', 'spread hate',
            'target minorities', 'attack ethnic',
            'homophobic slur', 'transphobic attack',
            'nazi propaganda', 'white supremacy', 'kkk',
            'genocide plan', 'ethnic cleansing'
        ],
        'el': [
            'ρατσιστική επίθεση', 'διακριτική μεταχείριση',
            'ομοφοβική επίθεση', 'μίσος κατά'
        ]
    },
   
    # ─── FRAUD & SCAMS ───
    'fraud': {
        'en': [
            'ponzi scheme', 'pyramid scheme', 'multi level
marketing scam',
            'fake invoice', 'invoice fraud', 'billing fraud',
            'insurance fraud', 'tax evasion', 'money laundering',
            'counterfeit money', 'print fake money', 'fake
currency',
            'romance scam', 'catfish', 'advance fee fraud',
            'wire fraud', 'bank fraud', 'loan fraud',
            'fake charity', 'donation scam'
        ],
        'el': [
            'πυραμίδα απάτης', 'απάτη ασφάλισης',
            'φορολογική απάτη', 'ξέπλυμα χρήματος',
            'πλαστά χρήματα', 'ψεύτικη φιλανθρωπία'
        ]
    },
   
    # ─── DOXXING & PRIVACY VIOLATIONS ───
    'doxxing': {
        'en': [
            'find home address', 'dox someone', 'doxxing',
            'find phone number', 'personal information',
            'track location', 'stalk someone', 'stalking',
            'find someone address', 'expose personal info',
            'revenge leak', 'leak personal data'
        ],
        'el': [
            'βρες διεύθυνση', 'παρακολουθώ κάποιον',
            'βρες τηλέφωνο', 'προσωπικές πληροφορίες',
            'εντοπισμός θέσης'
        ]
    },
   
    # ─── PLAGIARISM & AI MISUSE ───
    'ai_misuse': {
        'en': [
            'write my entire thesis', 'write my dissertation',
            'complete my coursework', 'do all my homework',
            'pretend to be me', 'impersonate student',
            'bypass ai detection', 'avoid ai detector',
            'humanize ai text', 'make ai undetectable'
        ],
        'el': [
            'γράψε την διπλωματική μου', 'κάνε την εργασία μου
ολόκληρη',
            'παράκαμψη ανίχνευσης ai', 'αποφυγή ai detector'
        ]
    }
}
#
═══════════════════════════════════════════════════════════════════════════════
#                              PROFANITY DATABASE
#
═══════════════════════════════════════════════════════════════════════════════
PROFANITY_WORDS = {
    'en': [
        # Strong profanity (blocked)
        'fuck', 'f*ck', 'fuk', 'fck', 'fuking', 'fucking',
'fucked', 'fvck',
        'shit', 'sh*t', 'sht', 'shlt', 'shitty',
'bullshit',
        'bitch', 'b*tch', 'btch', 'bitchy', 'biatch',
        'ass', 'asshole', 'a**hole', 'arse', 'arsehole',
        'damn', 'dammit', 'goddamn', 'goddammit',
        'cunt', 'c*nt', 'cnt',
        'dick', 'd*ck', 'dck', 'dickhead',
        'piss', 'p*ss', 'pissed', 'pissing',
        'bastard', 'bstrd', 'bastrd',
        'whore', 'wh*re', 'slut', 'sl*t',
        'cock', 'c*ck', 'cck', 'pussy', 'psy',
        'fag', 'faggot', 'f*g', 'fgt',
        'retard', 'retarded', 'rtrd',
        'nigger', 'nigga', 'n*gger', 'n*gga',
        'kike', 'chink', 'gook', 'spic',
        'wanker', 'wank', 'bollocks', 'bugger',
        'prick', 'twat', 'crap', 'crappy'
    ],
    'el': [
        # Greek profanity
        'μαλάκας', 'malaka', 'μαλακα', 'μλκ', 'mlk',
        'πούστης', 'πουστη', 'πστ', 'poustis',
        'γαμώ', 'γαμω', 'gamo', 'γμτ', 'gmt',
        'γαμημένος', 'gamimenos', 'γμν',
        'σκατά', 'skata', 'σκτ', 'skt',
        'αρχίδι', 'αρχιδια', 'arxidi', 'ρχδ',
        'κώλος', 'kolos', 'kwlos', 'κλ',
        'τσούλα', 'tsoula', 'τσλ',
        'πουτάνα', 'poutana', 'πτν',
        'βλάκας', 'vlakas', 'βλκ',
        'μούνι', 'mouni', 'μν', 'mni'
    ]
}
#
═══════════════════════════════════════════════════════════════════════════════
#                           LEETSPEAK VARIATIONS
#
═══════════════════════════════════════════════════════════════════════════════
LEETSPEAK_MAP = {
    '4': 'a', '@': 'a',
    '3': 'e',
    '1': 'i', '!': 'i', '\|': 'i',
    '0': 'o',
    '5': 's', '$': 's',
    '7': 't',
    '8': 'b',
    '9': 'g'
}
#
═══════════════════════════════════════════════════════════════════════════════
#                         RESPONSE MESSAGES
#
═══════════════════════════════════════════════════════════════════════════════
BLOCK_MESSAGES = {
    'violence': {
        'en': "🚫 I cannot provide information about violence,
weapons, or causing harm. If you're experiencing thoughts of harming
yourself or others, please contact a crisis helpline immediately.",
        'el': "🚫 Δεν μπορώ να παρέχω πληροφορίες για βία, όπλα ή
πρόκληση βλάβης. Αν αντιμετωπίζετε σκέψεις αυτοβλάβης ή βλάβης άλλων,
επικοινωνήστε άμεσα με γραμμή κρίσης."
    },
    'drugs': {
        'en': "🚫 I cannot provide information about illegal drug
manufacturing, distribution, or use. If you need help with substance
abuse, please contact a medical professional or support service.",
        'el': "🚫 Δεν μπορώ να παρέχω πληροφορίες για παράνομη
παρασκευή, διανομή ή χρήση ναρκωτικών. Αν χρειάζεστε βοήθεια,
επικοινωνήστε με ιατρικό επαγγελματία."
    },
    'hacking': {
        'en': "🚫 I cannot help with hacking, unauthorized access, or
any illegal cyber activities. If you're interested in cybersecurity, I
recommend studying ethical hacking through legitimate educational
programs.",
        'el': "🚫 Δεν μπορώ να βοηθήσω με χάκινγκ, μη εξουσιοδοτημένη
πρόσβαση ή παράνομες κυβερνοεπιθέσεις. Αν ενδιαφέρεστε για
κυβερνοασφάλεια, συνιστώ νόμιμα εκπαιδευτικά προγράμματα."
    },
    'cheating': {
        'en': "🚫 I cannot help with academic dishonesty, cheating,
or grade manipulation. These actions violate academic integrity
policies. I'm here to help you learn, not to circumvent the educational
process.",
        'el': "🚫 Δεν μπορώ να βοηθήσω με ακαδημαϊκή ανεντιμότητα,
αντιγραφή ή χειραγώγηση βαθμών. Αυτές οι ενέργειες παραβιάζουν την
ακαδημαϊκή ακεραιότητα."
    },
    'explicit': {
        'en': "🚫 I cannot provide any content related to child
exploitation, non-consensual intimate content, or illegal explicit
material. Such content is illegal and deeply harmful.",
        'el': "🚫 Δεν μπορώ να παρέχω περιεχόμενο που σχετίζεται με
εκμετάλλευση ανηλίκων ή παράνομο υλικό. Τέτοιο περιεχόμενο είναι
παράνομο και εξαιρετικά επιβλαβές."
    },
    'self_harm': {
        'en': "🚫 I'm concerned about your wellbeing. If you're
having thoughts of self-harm or suicide, please reach out for help:\n•
National Suicide Prevention Lifeline: 988 (US)\n• Crisis Text Line:
Text HOME to 741741\n• International: findahelpline.com",
        'el': "🚫 Ανησυχώ για την ευημερία σας. Αν έχετε σκέψεις
αυτοβλάβης, παρακαλώ ζητήστε βοήθεια:\n• Γραμμή Ζωής: 1018\n• Για
επείγουσα βοήθεια: 112"
    },
    'hate_speech': {
        'en': "🚫 I cannot provide content that promotes hate,
discrimination, or violence against any group. Everyone deserves respect
and dignity.",
        'el': "🚫 Δεν μπορώ να παρέχω περιεχόμενο που προωθεί το
μίσος, τις διακρίσεις ή τη βία κατά οποιασδήποτε ομάδας."
    },
    'fraud': {
        'en': "🚫 I cannot help with fraud, scams, or illegal
financial activities. These are serious crimes with severe legal
consequences.",
        'el': "🚫 Δεν μπορώ να βοηθήσω με απάτες ή παράνομες
οικονομικές δραστηριότητες. Αυτά είναι σοβαρά εγκλήματα με σοβαρές
νομικές συνέπειες."
    },
    'profanity': {
        'en': "⚠️ Please keep the conversation respectful. I'm here
to help with Open eClass questions in a professional manner.",
        'el': "⚠️ Παρακαλώ διατηρήστε τη συζήτηση με σεβασμό. Είμαι
εδώ για να βοηθήσω με ερωτήσεις Open eClass με επαγγελματικό τρόπο."
    },
    'default': {
        'en': "🚫 I cannot help with that request. I'm designed to
assist with legitimate Open eClass learning and usage questions. Is
there something educational I can help you with?",
        'el': "🚫 Δεν μπορώ να βοηθήσω με αυτό το αίτημα. Είμαι
σχεδιασμένος για να βοηθώ με νόμιμες εκπαιδευτικές ερωτήσεις Open
eClass. Υπάρχει κάτι εκπαιδευτικό με το οποίο μπορώ να βοηθήσω;"
    },
        'doxxing': {
        'en': "🚫 I cannot help with finding personal information,
tracking people, or any form of stalking or doxxing. These activities
are illegal and violate privacy rights.",
        'el': "🚫 Δεν μπορώ να βοηθήσω με εύρεση προσωπικών
πληροφοριών, παρακολούθηση ατόμων ή οποιαδήποτε μορφή παρενόχλησης.
Αυτές οι δραστηριότητες είναι παράνομες."
    },
    'ai_misuse': {
        'en': "🚫 I'm here to help you learn, not to complete your
work for you. Academic integrity is important. I can:\n• Explain
concepts\n• Provide examples\n• Guide your research\n• Review your
work\n\nBut I cannot write entire assignments for you.",
        'el': "🚫 Είμαι εδώ για να σας βοηθήσω να μάθετε, όχι να κάνω
τη δουλειά σας. Η ακαδημαϊκή ακεραιότητα είναι σημαντική. Μπορώ να:\n•
Εξηγήσω έννοιες\n• Δώσω παραδείγματα\n• Καθοδηγήσω την έρευνά σας\n•
Ελέγξω τη δουλειά σας\n\nΑλλά δεν μπορώ να γράψω ολόκληρες εργασίες
για εσάς."
    },
   
}
