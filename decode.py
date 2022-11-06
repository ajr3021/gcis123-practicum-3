"""
Given a file containing words written as a series of
numbers, representing their number value on the ascii chart,
separated by spaces, turn those numbers into strings.

You will then need to return the strings in a data structure
that can easily allow the user to search for all words
starting with a certain letter. 
"""
def read_and_decode(filename):
    with open(filename) as file_:
        word_dict = dict()
        for line in file_:
            word = ""
            line = line.strip().split(' ')
            for num in line:
                word += chr(int(num))
            
            if word[0] in word_dict:
                word_dict[word[0]].append(word)
            else:
                word_dict[word[0]] = [word]
    return word_dict

"""
Given the data structure used in the last function,
return all words starting with the given letter.
"""
def search(letter, data):
    return data[letter]


def main():
    data = read_and_decode("data/words.txt")
    letter = input("Enter a letter: ")
    print(search(letter, data))


if __name__ == '__main__':
    main()