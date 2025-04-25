from stats import get_word_count

def main():
    # book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count("books/frankenstein.txt")
    print(f"{word_count} words found in the document.")

main()