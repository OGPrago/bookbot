def get_word_count(filepath):
    with open(filepath) as f:
        words = f.read()
        return len(words.split())

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_character_count(book_text):
        characters = {}
        for c in book_text:
            lowered = c.lower()
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
        return characters
            