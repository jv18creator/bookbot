from stats import get_book_text, sorted_characters
import sys

def main():
    print("============ BOOKBOT ============", sys.argv)

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_name = sys.argv[1]


    print(f"Analyzing book found at {book_name}...")
    book_text = get_book_text(book_name)
    print("----------- Word Count ----------")
    print(f"Found {len(book_text.split())} total words")

    print("--------- Character Count -------")
    character_counts = sorted_characters(book_text)
    for char in character_counts:
        print(f"{char['char']}: {char['num']}")

main()
