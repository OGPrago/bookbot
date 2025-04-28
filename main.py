from stats import get_word_count
from stats import get_character_count
from stats import get_book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    
    word_count = get_word_count("books/frankenstein.txt")
    # print(f"{word_count} words found in the document.")
    
    chars_dict = get_character_count(book_text)
    print(f"{word_count} words found in the document.")
    print(chars_dict)
main()