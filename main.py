import sys

from stats import get_num_words, get_character_count, get_sorted_chars

if len(sys.argv) != 2:
    print("Usage:python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    total_words = get_num_words(text)
    char_count = get_character_count(text)
    sorted_chars = get_sorted_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()