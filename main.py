def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars = get_chars_dict(text)
    print(text)
    print(f"{words} words found in the document")
    print(chars)
def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count
def get_chars_dict(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()
