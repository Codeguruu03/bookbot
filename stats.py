def char_count(text: str) -> dict:
    """Counts how many times each character appears in the text."""
    text = text.lower()
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1

    return counts


def sort_characters(counts: dict) -> list:
    """Takes dictionary of char counts and returns a sorted list of dicts."""
    # Build list of dicts in form {"char": c, "num": n}, skipping non-alpha chars
    chars = [{"char": c, "num": n} for c, n in counts.items() if c.isalpha()]

    # Sort descending by "num"
    chars.sort(key=lambda x: x["num"], reverse=True)

    return chars
