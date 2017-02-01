import urllib
import string

link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'

story_file = urllib.urlopen(link)
story = story_file.read()
story_list = story.split()

def trim_punctuation(story_list):
    story_list = [''.join(c for c in s if c not in string.punctuation) for s in story_list]
    story_list = [s for s in story_list if s]

def histogram():
    trim_punctuation(story_list)
    tuple_of_unique_words = ()
    print(len(story_list))
    # for word in range(0, len(story_list))
histogram()
