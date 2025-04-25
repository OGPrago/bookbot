def main():
    # book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count("books/frankenstein.txt")
    print(f"{word_count} words found in the document.")

def get_word_count(filepath):
    with open(filepath) as f:
        words = f.read()
        return len(words.split())

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()