def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars = get_chars_dict(text)
    list_of_chars = [{'key': k, 'value':v} for k, v in chars.items()]
    list_of_chars.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    my_report = print_report(list_of_chars)
    print("--- End report ---")
def print_report(list):
    for el in list:
        if el['key'].isalpha():
            print(f"The '{el['key']}' character was found {el['value']} times")
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
def sort_on(dict):
    return dict['value']
main()
