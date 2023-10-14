def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    sorted_letter_count = list(letter_count.items())
    sorted_letter_count.sort(key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char, count in sorted_letter_count:
        print(f"The {char} character was found {count} times")
    print("--- End report ---")

def get_letter_count(text):
    letters = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else :
                letters[char] = 1
    return letters

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()