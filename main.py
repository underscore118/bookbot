def main():
    
    from stats import get_number_words
    from stats import get_chars_dict
    from stats import get_report

    book_path = "books/frankenstein.txt"
    text_content = get_book_text(book_path)
    Nletter = {}
    report = {}


    Nword = f"{get_number_words(text_content)}"
    Nletter = get_chars_dict(text_content)
    report = get_report(Nletter)
    
    print_repo(book_path, Nword, report)


    #print(report)
    #print(Nletter)
    #print(Nword)


def get_book_text(path_file):
    with open(path_file) as f:
       return f.read()
    
def print_repo(book_path, Nwords, report):
    print("============ BOOKBOT ============")
    print("Analyzing book found at "+ book_path)
    print("----------- Word Count ----------")
    print("Found " + Nwords + " total words")
    print("--------- Character Count -------")


    for item in report:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]} ")


    print("============= END ===============")
    
 
    return None




main()









