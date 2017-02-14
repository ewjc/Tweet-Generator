import sys
import random
import histogram

# def return_random_word(story_list):
#     rand_index = random.randint(0, len(story))
#     word = story[rand_index]
#     for word in
#     print(word)

def sample_random_word(dict_unique_words):
    rand_index = random.randint(1, sum(dict_unique_words))
    probability_count = 0
    for word, frequency in dict_unique_words:
        if rand_index >= probability_count:
            probability_count += frequency
        return word
        
if __name__ == '__main__':
    histogram()
    frequency()
    return_random_word
