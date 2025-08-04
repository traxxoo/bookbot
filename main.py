from stats import return_count
from stats import letter_count
from stats import listing_the_dict
import sys 


def get_book_text(filepath):
    with open(filepath) as f:
        file_conents = f.read()
        return file_conents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_material = get_book_text(sys.argv[1])

    word_count = return_count(file_material)
    each_letter_count = letter_count(file_material)
    
    char_list = listing_the_dict(each_letter_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for data in char_list:
        if data["char"].isalpha() :
            print(f"{data["char"]}: {data["num"]}")


main()
