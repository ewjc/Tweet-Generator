import sys
import random
import urllib

link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'

text_file = urllib.urlopen(link)
story_list = text_file.read()
story = story_list.split()
