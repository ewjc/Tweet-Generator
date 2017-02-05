import sys
import random
import urllib

link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'

text_file = urllib.urlopen(link)
story_list = text_file.read()
story = story_list.split()

def return_random_word(story):
    rand_index = random.randint(0, len(story))
    word = story[rand_index]
    print(word)

return_random_word(story)
