import sys
import random
import urllib

link = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'

user_input = sys.argv[1:]
text_file = urllib.urlopen(link)
story_list = text_file.read()
story = story_list.split()

def return_random_word(story):
    rand_index = random.randint(0, len(story))
    word = story[rand_index]
    for index in range(0, 5):
        print(word)

return_random_word(story)
