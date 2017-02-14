import sys

def read_story(text):
    with open(text) as bible:
        story = bible.read()
    word_list = story.split()

    return word_list

def trim_punctuation_from_word(word):
    char_list = []
    for char in word:
        if char not in string.punctuation:
            char_list.append(char)
    trimmed_word = ''.join(char_list)
    return trimmed_word

def trim_punctuation(word_list):
    # step 1: remove punctuation characters from each word
    # remove punctuation characters from each word and remove any empty strings (len==0)
    word_list1 = []
    for word in word_list:
        trimmed_word = trim_punctuation_from_word(word)
        if len(trimmed_word) > 0:
            word_list1.append(trimmed_word)
    return word_list1

def

if __name__ == '__main__':
    text = 'Bible.txt'
