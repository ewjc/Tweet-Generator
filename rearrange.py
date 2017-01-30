import random
import sys

arg = sys.argv[1:]
arg_length = len(arg) - 1
print(arg)

def randomize_words():
    rand_index = random.randint(0, arg_length)
    for i in (0, arg_length):
        temp = arg[i]
        arg[i] = arg[rand_index]
        temp = arg[rand_index]
    return arg

if __name__ == '__main__':
    words = randomize_words()
    print(words)
