from corpus_loader import word_list, name_list
import re

test_words = [
     "a dark and stormy night",
    "n qnex naq fgbezl avtug",
    "j mjat jwm bcxavh wrpqc",
    "call me Ishmael",
    "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
]

def count_words(text):

    test_words = text.split()

    word_count = 0

    for test_word in test_words:
        word = re.sub(r'[^A-Za-z]+','', test_word)
        # word = test_word
        if word.lower() in word_list or word in name_list:
            print("english word", word)
            word_count += 1
        else:
            print('not english word or name', word)
            pass

    return word_count

for phrase in test_words:
    word_count = count_words(phrase)
    percentage = int(word_count / len(phrase.split()) * 100)
    print(phrase, percentage)