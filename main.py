def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    print(text)
    print(f"{words} words found in the document")
def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

main()
