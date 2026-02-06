import re


def normalize_arabic(text):
    # 1. Remove standard diacritics (Tashkeel)
    # Range includes: Fatha, Damma, Kasra, Shadda, Sukun, Tanween, etc.
    text = re.sub(r'[\u064B-\u0652]', '', text)

    # 2. Remove Quranic-specific diacritics & Tatweel (Kashida)
    # \u0670 = Superscript Alif (found in words like 'haza' in Quran)
    # \u0640 = Tatweel (stretching line, e.g., بـــ)
    text = re.sub(r'[\u0640\u0670]', '', text)

    # 3. STRICT RULE: Do NOT normalize Alif (أ, إ, آ) to Bare Alif (ا).
    # If you strictly want 'Correct' Arabic, keep the Hamzas.
    # (If you prefer 'Search/Google' style normalization, uncomment the line below)
    # text = re.sub(r'[إأآ]', 'ا', text)

    # 4. STRICT RULE: Do NOT normalize Alif Maqsura (ى) to Ya (ي).
    # This prevents the "Salla" -> "Salli" error.

    # 5. Remove punctuation and non-word characters
    # Note: We use \w to keep all Arabic letters and numbers.
    text = re.sub(r'[^\w\s]', '', text)

    # 6. Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# Input Text
input_text =""

# Output
cleaned_text = normalize_arabic(input_text)
print(cleaned_text)