import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    location = sys.argv[1]
    file = get_book_text(location)
    count = count_words(file)
    counts = count_characters(file)
    counts = sort_characters(counts)

    print(
        f"""
============ BOOKBOT ============
Analyzing book found at {location}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------
        """
    )
    for i in counts:
            print(f"{i["character"]}: {i["num"]}")

main()