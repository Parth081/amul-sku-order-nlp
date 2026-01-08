import re

INTENT_WORDS = {
    "book","order","buy","need","want","give","send",
    "place","add","require","purchase","chahiye","dedo"
}

CONTROL_WORDS = {
    "qty","quantity","count","number","nos","no",
    "pieces","pcs","packet","pack","bottle","box"
}

CONVERSATION_WORDS = {
    "please","pls","plz","ok","okay","haan","han",
    "yes","yeah","bhai","sir","madam","ji","boss"
}

STRUCTURAL_WORDS = {
    "in","of","for","to","from","with","and",
    "me","my","is","are","do","does","this","that"
}

JUNK_WORDS = (
    INTENT_WORDS |
    CONTROL_WORDS |
    CONVERSATION_WORDS |
    STRUCTURAL_WORDS
)

UNITS = {"ml","l","gm","kg"}

def preprocess_text(text: str) -> str:
    text = text.lower()

    # 🔥 critical fix
    text = re.sub(r"(\d+\.?\d*)(ml|l|gm|kg)", r"\1 \2", text)

    text = re.sub(r"[^\w\s\.]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = text.split()

    cleaned = []
    seen_brand = False

    for token in tokens:

        if re.fullmatch(r"\d+\.?\d*", token):
            cleaned.append(token)
            continue

        if token in UNITS:
            cleaned.append(token)
            continue

        if token == "amul":
            seen_brand = True
            cleaned.append(token)
            continue

        if seen_brand:
            cleaned.append(token)
            continue

        if token in JUNK_WORDS:
            continue

    text = " ".join(cleaned)

    # reorder if quantity comes first
    match = re.match(r"^(\d+\.?\d*\s*(ml|l|gm|kg))\s+(amul.*)", text)
    if match:
        text = f"{match.group(3)} {match.group(1)}"

    return text
