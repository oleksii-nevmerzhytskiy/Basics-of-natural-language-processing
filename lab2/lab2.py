import re
from nltk.stem import PorterStemmer
from nltk.tokenize import MWETokenizer
import collections
import math


def non_letter(str):
    return re.sub("[0-9\W_]", " ", str)


def tokenization(str):
    tokenizer = MWETokenizer()
    return tokenizer.tokenize(str.split())


def stemmer_list(word_list):
    stemmer = PorterStemmer()
    stemmer_word_list = [stemmer.stem(word) for word in word_list]
    return stemmer_word_list


def term_frequency(word_list):
    tf_text = collections.Counter(word_list)
    count = len(word_list)
    for i in tf_text:
        tf_text[i] = tf_text[i] / count
    return tf_text


def compute_idf(word, corpus):
    return math.log10(len(corpus) / sum([1 for i in corpus if word in i]))


def tf_idf(word_list, corpus):
    tf = term_frequency(word_list)
    dictionary = {word: compute_idf(word, corpus) for word in word_list}

    for word in tf:
        tf[word] = (dictionary[word] * tf[word])
    return tf


my_file = open("moviereviews_100.tsv", "r", encoding="UTF-8")
my_string = my_file.read().split('"\nneg	"')
my_file.close()
q = [w for w in my_string if w != '']
for i in range(len(q)):
    q[i] = non_letter(q[i])
    q[i] = tokenization(q[i])
    q[i] = stemmer_list(q[i])

my_file = open("output.txt", "w", encoding="UTF-8")
my_file.write("")
my_file.close()

for i in range(10):
    rez = tf_idf(q[i], q)
    my_file = open("output.txt", "a", encoding="UTF-8")
    my_file.write(str(rez) + "\n\n")
    my_file.close()
    print(rez)
