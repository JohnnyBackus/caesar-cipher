from corpus_loader import word_list, name_list
import re


def validate_words(text):

    def count_words(text):
        text_split = text.split()
        word_count = 0

        for expression in text_split:
            word = re.sub(r'[^A-Za-z]+','', expression)
            if word.lower() in word_list or word in name_list:
                print("english word:", word)
                word_count += 1
            else:
                print("Not english word or name:", word)

        return word_count
    
    word_count = count_words(text)
    percentage = int(word_count / len(text.split()) * 100)
    print(f"text: '{text}' | percent word/name match: {percentage}%")
    
    if percentage > 50:
        return True


if __name__ == "__main__":
    
    test_phrases = [
    "a dark and stormy night   rains cats and dogs",
    ", fasd 3213 4 t Joey? @ $ !",
    "n qnex naq fgbezl avtug",
    "j mjat jwm bcxavh wrpqc",
    "call me Ishmael",
    "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
    ]

    print(validate_words(test_phrases))
