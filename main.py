def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    sorted_list = sorted([{'letter': k, 'num': v} for k, v in num_chars.items()], key=lambda x: x['num'], reverse=True)
    for element in sorted_list:
        print(f"The '{element['letter']}' character was found {element['num']} times")
    print("\n--- End report ---")

def sort_on(dict):
    return dict[""]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    lower_str = text.lower()
    for c in lower_str:
        if(c.isalpha()):
            chars[c] = chars[c] + 1 if (c in chars) else 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()