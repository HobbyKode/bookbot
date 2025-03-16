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
            chars[lowered] = 1
    return  chars


def sort_on(dict):
    return dict["num"]

def generate_report(book_path, num_words, chars_dict):
    title = "Frankenstein"
    #Convert the dictionary into a list to simplify the sort
    freq_list = [{"char": char, "num": count} for char, count in chars_dict.items()]
    #Non-chronological order sorting
    freq_list.sort(key =sort_on, reverse = True)


    #Displaying my report
    print(f"============ BOOKBOT ============")
    print(f"--- Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    #Only displaying letters from the Alphabet
    for item in freq_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print(f"============ END ============")
