"""
Given two filenames, return all of the words that are in both
files as whatever data structure you feel is most appropriate.
"""
def common_words(filename1, filename2):
    words1 = find_words(filename1)
    words2 = find_words(filename2)

    words_both = set()

    for word in words1:
        if word in words2:
            words_both.add(word)

    return words_both

"""
Helper function to reduce repeat code
"""
def find_words(filename):
    word_set = set()
    with open(filename) as file_:
        for line in file_:
            line = line.strip().split()
            for word in line:
                word_set.add(word)
    return word_set


def main():
    words = common_words("data/starwars.txt", "data/raven.txt")
    print(words)

if __name__ == '__main__':
    main()