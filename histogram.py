import urllib
import string
import sys

link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'

arg = sys.argv[1]
story_file = urllib.urlopen(link)
story = story_file.read()
story_list = story.split()
dict_unique_words = dict()

def trim_punctuation(story_list):
    story_list = [''.join(c for c in s if c not in string.punctuation) for s in story_list]
    story_list = [s for s in story_list if s]

def histogram():
    trim_punctuation(story_list)
    for index_story_list in range(0, len(story_list)):
        stored_word = story_list[index_story_list]
        if stored_word not in dict_unique_words:
            dict_unique_words.update({stored_word : 1})
        elif stored_word in dict_unique_words:
            dict_unique_words[stored_word] += 1

def unique_words_count():
    print(len(dict_unique_words))

def frequency():
    if arg in dict_unique_words:
        print('Frequency of word: ' + str(dict_unique_words[arg]))
    elif arg not in dict_unique_words:
        print('Frequency of word: 0')

if __name__ == '__main__':
    histogram()
    print('There are a total of {unique_words_count} words.'.format(unique_words_count=len(dict_unique_words)))
    frequency()
