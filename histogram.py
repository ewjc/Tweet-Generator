import urllib
import string
import sys

arg = sys.argv[1:]
link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'

story_file = urllib.urlopen(link)
story = story_file.read()
story_list = story.split()
dict_unique_words = {}

def trim_punctuation(story_list):
    story_list = [''.join(c for c in s if c not in string.punctuation) for s in story_list]
    story_list = [s for s in story_list if s]

def histogram():
    trim_punctuation(story_list)
    for index_story_list in range(0, len(story_list)):
        stored_word = story_list[index_story_list]
        if stored_word not in dict_unique_words:
            dict_unique_words.add(stored_word=1)
        elif stored_word in dict_unique_words:
            dict_unique_words[stored_word] += 1
histogram()
