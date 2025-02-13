#Open that file
def main():
    title = "Frankenstein"
    #Define path in a variable
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the book '{title}'")



def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
        return book_contents

main()

