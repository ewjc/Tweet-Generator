import urllib
import string
import sys

link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'

arg = sys.argv[1]
story_file = urllib.urlopen(link)
story = story_file.read()
word_list = story.split()
dict_unique_words = dict()

def trim_punctuation(word_list):
    word_list = [''.join(c for c in s if c not in string.punctuation) for s in word_list]
    word_list = [s for s in word_list if s]

def histogram():
    trim_punctuation(word_list)
    for index_word_list in range(0, len(word_list)):
        stored_word = word_list[index_word_list]
        if stored_word not in dict_unique_words:
            dict_unique_words.update({stored_word : 1})
        elif stored_word in dict_unique_words:
            dict_unique_words[stored_word] += 1
    print('There are a total of {unique_words_count} unique words.'.format(unique_words_count=len(dict_unique_words)))

def frequency():
    if arg in dict_unique_words:
        print('Frequency of word: ' + str(dict_unique_words[arg]))
    else:
        print('Frequency of word: 0')

def sort(dict_unique_words):
    for index in sorted(dict_unique_words, key = dict_unique_words.get, reverse=True):
        print(index, dict_unique_words[index])


if __name__ == '__main__':
    histogram()
    frequency()
    # sort()
