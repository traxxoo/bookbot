from stats import return_count
from stats import letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_conents = f.read()
        return file_conents

def main():
    file_material = get_book_text("books/frankenstein.txt")
    word_count = return_count(file_material)
    print(f"{word_count} words found in the document")
    each_letter_count = letter_count(file_material)
    print(each_letter_count)



main()
