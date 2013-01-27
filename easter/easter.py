from collections import Counter
import math

#easter_alphabet = {'a': 56, 'b': 34, 'c': 27,
#                   'd': 28, 'e': 64, 'f': 13,
#                   'g': 15, 'h': 13, 'i': 24,
#                   'j': 1,  'k': 6,  'l': 63,
#                   'm': 11, 'n': 67, 'o': 21,
#                   'p': 11, 'q': 3,  'r': 61,
#                   's': 73, 't': 71, 'u': 14,
#                   'v': 17, 'w': 8,  'x': 3,
#                   'y': 33, 'z': 1}

def calculate_word_value(word, easter_alphabet):
    total = 0
    word = word.lower().translate(None, ' ')
    for character in word:
        total += easter_alphabet[character]

    return total

def generate_frequency():
    counter = Counter()
    with open('/vhome/words') as lines:
        for line in lines:
            counter.update(line.lower().strip())
    return counter

def generate_alpha_weight(frequencies):
    overall_count = sum(frequencies.values())
    weight = lambda value: math.floor(float(value)/overall_count * 1000)
    weights = {key: weight(value) for key, value in frequencies.items()}
    return weights


