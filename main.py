from stats import get_num_words


#Open that file
def main():
    #Define path in a variable
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #Calling the function counting characters
    chars_dict = get_chars_dict(text)

    generate_report(book_path, num_words, chars_dict)





def get_chars_dict(text):
    chars = {}

    #checking each character in a lowercase string
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return  chars


def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
        return book_contents


def sort_on(dict):
    return dict["num"]

def generate_report(book_path, num_words, chars_dict):
    title = "Frankenstein"
    #Convert the dictionary into a list to simplify the sort
    freq_list = [{"char": char, "num": count} for char, count in chars_dict.items()]
    #Non-chronological order sorting
    freq_list.sort(key =sort_on, reverse = True)


    #Displaying my report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the book '{title}'")
    #Only displaying letters from the Alphabet
    for item in freq_list:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")

main()