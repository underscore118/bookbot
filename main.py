def main():
    
    from stats import get_number_words
    from stats import get_chars_dict


    book_path = "books/frankenstein.txt"
    text_content = get_book_text(book_path)
    Nletter = {}


    Nword = f"{get_number_words(text_content)} words found in the document"
    Nletter = get_chars_dict(text_content)
    
    print(Nletter)
    print(Nword)


def get_book_text(path_file):
    with open(path_file) as f:
       return f.read()




main()









