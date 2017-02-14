class Histogram(dict):

def __init__(self, iterable=None):
    super(Histogram, self).__init__()
    self.types = 0  # the number of distinct item types in this histogram
    self.tokens = 0  # the total count of all item tokens in this histogram

def find_unique_words_and_frequency(self):
    for index_word_list in range(0, len(word_list)):
        stored_word = word_list[index_word_list]
        if stored_word not in dict_unique_words:
            dict_unique_words.update({stored_word : 1})
        elif stored_word in dict_unique_words:
            dict_unique_words[stored_word] += 1
    return

def frequency(arg):
    if arg in dict_unique_words:
        print('Frequency of word: ' + str(dict_unique_words[arg]))
    else:
        print('Frequency of word: 0')
