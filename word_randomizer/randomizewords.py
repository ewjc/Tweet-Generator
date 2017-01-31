import sys
import random

arg = sys.argv[1]

words_file = open('/usr/share/dict/words', 'r')
words_list = words_file.readlines()
message = ''

for index in range(1, int(arg)):
    rand_index = random.randint(0, len(words_list))
    word = words_list[rand_index]
    message += word.replace('\n', ' ')

print(message)
