def main():
    book_path="books/frankenstein.txt"
    text=get_book_text(book_path)
    num_words=count_words(text)
    char_count=count_chars(text)
    print(f"{num_words} words found in the document.")
    print(count_chars(text))
    

def get_book_text(path):
     with open(path) as f:
        return f.read()
    
def count_words(text):
    words=text.split()
    return len(words)

def count_chars(text):
    char_dict={}
    for char in text.lower():
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
    return char_dict
     
main()