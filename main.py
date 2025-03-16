from stats import get_num_words, get_chars_dict, generate_report
import sys
#Open that file
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #Calling the function counting characters
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(f"{chars_dict}")
    generate_report(book_path, num_words, chars_dict)

def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
        return book_contents


main()