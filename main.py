import sys
from stats import char_count, sort_characters

def get_book_text(filepath):
    """Reads and returns the contents of the file at the given filepath."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text: str) -> int:
    """Counts the words in the given text and returns the total."""
    words = text.split()
    return len(words)

def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    # Word count
    num_words = count_words(text)

    # Character count and sorting
    char_stats = char_count(text)
    sorted_chars = sort_characters(char_stats)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
