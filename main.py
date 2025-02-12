#Define path in a variable
path_to_file = "books/frankenstein.txt"
title = "Frankenstein"

#Open that file
def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

main()