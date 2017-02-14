import urllib
import string
import sys


def read_bible():
    ### These 3 lines download a text file from the Web!
    # link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'
    # story_file = urllib.urlopen(link)
    # story = story_file.read()
    ### These 2 lines open the text file from your computer
    with open('Bible.txt') as bible:
        story = bible.read()

    word_list = story.split()
    return word_list

dict_unique_words = dict()

def trim_punctuation_from_word(word):
    char_list = []
    for char in word:
        if char not in string.punctuation:
            char_list.append(char)
    trimmed_word = ''.join(char_list)
    return trimmed_word

def trim_punctuation(word_list):
    # step 1: remove punctuation characters from each word
    # word_list1 = [''.join(c for c in s if c not in string.punctuation) for s in word_list]
    # # equivalent to:
    # word_list1 = []
    # for word in word_list:
    #     word_list1.append(''.join(c for c in s if c not in string.punctuation))
    # also equivalent to:
    # remove punctuation characters from each word
    # and remove any empty strings (len == 0)
    word_list1 = []
    for word in word_list:
        trimmed_word = trim_punctuation_from_word(word)
        if len(trimmed_word) > 0:
            word_list1.append(trimmed_word)

    # step 2: remove any empty strings (len == 0)
    # word_list2 = [word for word in word_list1 if len(word) > 0]
    # # equivalent to:
    # word_list2 = []
    # for word in word_list1:
    #     if len(word) > 0:
    #         word_list2.append(word)
    return word_list1

def histogram(word_list):
    for index_word_list in range(0, len(word_list)):
        stored_word = word_list[index_word_list]
        if stored_word not in dict_unique_words:
            dict_unique_words.update({stored_word : 1})
        elif stored_word in dict_unique_words:
            dict_unique_words[stored_word] += 1
    sort()
    print('There are a total of {unique_words_count} unique words.'.format(unique_words_count=len(dict_unique_words)))


def frequency(arg):
    if arg in dict_unique_words:
        print('Frequency of word: ' + str(dict_unique_words[arg]))
    else:
        print('Frequency of word: 0')

def sort():
    for index in sorted(dict_unique_words, key = dict_unique_words.get, reverse=True):
        print(index, dict_unique_words[index])
#
# def return_random_word(dict_unique_words):
#     rand_index ``= random.randint(0, len(dict_unique_words))
#     word = word_list[rand_index]
#     print(word)

def check_bible_word_frequency(word_to_check):
    # Functional way:
    bible_words = read_bible()
    trimmed_bible_words = trim_punctuation(bible_words)
    bible_histogram = histogram(trimmed_bible_words)
    word_freq = frequency(bible_histogram, word_to_check)
    print "Frequency of {} is {}".format(word_to_check, word_freq)

if __name__ == '__main__':
    args_list = sys.argv
    if len(args_list) >= 2:
        word = args_list[1]
        print "You gave the word:", word
    else:
        word = 'Holy'
        print "Default word:", word

    check_bible_word_frequency(word)

    # histogram()
    # frequency()
    # return_random_word
