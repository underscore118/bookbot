
import sys


def main():
    
    from stats import get_number_words
    from stats import get_chars_dict
    from stats import get_report


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]


    text_content = get_book_text(book_path)
    Nletter = {}
    report = {}


    Nword = f"{get_number_words(text_content)}"
    Nletter = get_chars_dict(text_content)
    report = get_report(Nletter)
    
    print_repo(book_path, Nword, report)



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









