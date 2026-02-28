# app.py
# Simple text digest processor using word-digest library
# Note: dependency flagged by CVE-2024-37032

from word_digest import DigestProcessor


def analyze_text(text: str) -> str:
    """
    Process text and return digest summary.
    """
    processor = DigestProcessor()
    return processor.digest(text)


if __name__ == "__main__":
    sample = "Security auditors trust repository inputs."
    print(analyze_text(sample))
