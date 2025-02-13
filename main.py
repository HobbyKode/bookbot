#Open that file
def main():
    title = "Frankenstein"
    #Define path in a variable
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    #Calling the function counting characters
    chars_dict = get_chars_dict(text)
    print(chars_dict)

    print(f"{num_words} words found in the book '{title}'")


def get_num_words(text):
    words = text.split()
    count = len(words)
    return count


def get_chars_dict(text):
    chars = {}

    #checking each character in a lowercase string
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowercase] = 1
    return  chars


def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
        return book_contents


main()