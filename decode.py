"""
Given a file containing words written as a series of
numbers, representing their number value on the ascii chart,
separated by spaces, turn those numbers into strings.

You will then need to return the strings in a data structure
that can easily allow the user to search for all words
starting with a certain letter. 
"""
def read_and_decode(filename):
    pass

"""
Given the data structure used in the last function,
return all words starting with the given letter.
"""
def search(letter, data):
    pass


def main():
    data = read_and_decode("data/words.txt")
    letter = input("Enter a letter: ")
    print(search(letter, data))


if __name__ == '__main__':
    main()