import re
from nltk.tokenize import MWETokenizer
from nltk.corpus import stopwords

from stop_words import get_stop_words

import ukrainian_stemmer
import simplemma


# from nltk.stem import WordNetLemmatizer
# porter_stemmer = WordNetLemmatizer('ukrainian')


def non_letter(str):
    return re.sub("[0-9\W_]", " ", str)


def tokenization(str):
    tokenizer = MWETokenizer()
    return tokenizer.tokenize(str.split())


def delete_stop_words(word_list):
    stop_words = list(get_stop_words('ukrainian') + stopwords.words('russian'))
    stops = set(stop_words)

    filtered_word_list = word_list[:]
    for word in word_list:
        if word in stops:
            filtered_word_list.remove(word)
    return filtered_word_list


def lower_list(word_list):
    lower_word_list = [word.lower() for word in word_list]
    return lower_word_list


def stemmer_list(word_list):
    stemmer_word_list = [ukrainian_stemmer.UkrainianStemmer(word).stem_word() for word in word_list]
    return stemmer_word_list


def lemization_list(word_list):
    langdata = simplemma.load_data('uk')
    lemization_word_list = [simplemma.lemmatize(word, langdata) for word in word_list]
    return lemization_word_list


my_file = open("input.txt", "r", encoding="UTF-8")
my_string = my_file.read()
my_file.close()

my_string = non_letter(my_string)
my_string = tokenization(my_string)
my_string = lower_list(my_string)
my_string = delete_stop_words(my_string)
# my_string = stemmer_list(my_string)
my_string = lemization_list(my_string)
print(my_string)

my_file = open("output.txt", "w", encoding="UTF-8")
for word in my_string:
    my_file.write(word + " ")
my_file.close()
