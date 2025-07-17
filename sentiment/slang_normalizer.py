
import re

slang_dict = {
    "buda": "old man",
    "dai": "brother",
    "chatxan": "talks nonsense",
    "lyang hanxan": "speak nonsense",
    "lyan": "nonsense",
    "dami": "awesome",
    "ustei": "the same",
    "boro": "bro",
    "ghataudai": "reducing",
    "k vannu": "what to say",
    "bhako": "happened",
    "vayo": "done",
    "vane": "if",
    "xa": "is",
    "chan": "are",
    "sab": "everyone",
    "nai": "really",
    "ekdam": "very",
    "kati": "so many",
    "la": "",   
    "ani": "then",
    "ho": "is",
    "chha": "is",
    "ma": "in",
    "hoina": "is not"
}

def normalize_slang(text):
    text = text.lower()
    for slang, eng in slang_dict.items():
        text = re.sub(rf'\b{re.escape(slang)}\b', eng, text)
    return text
