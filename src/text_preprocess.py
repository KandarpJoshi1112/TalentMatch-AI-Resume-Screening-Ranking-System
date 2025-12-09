import re
import string

import pandas as pd

STOPWORDS = set([
    # Minimal stopwords for v1
    "the", "and", "is", "in", "to", "of", "a", "for", "on", "with", "at",
    "from", "by", "an", "be", "this", "that"
])

def clean_text(text: str) -> str:
    """
    Basic NLP cleaning:
    - Lowercase
    - Remove emails, urls, numbers
    - Remove punctuation
    - Remove stopwords
    """
    text = text.lower()

    # Remove emails and urls
    text = re.sub(r'\S+@\S+', ' ', text)
    text = re.sub(r'http\S+|www.\S+', ' ', text)

    # Remove numbers
    text = re.sub(r'\d+', ' ', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra spaces
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return " ".join(tokens)
