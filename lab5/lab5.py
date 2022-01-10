import tensorflow_hub as hub
from math import sqrt

my_file = open("corpus.txt", "r", encoding="UTF-8")
my_string = my_file.read().split('\n\n\n\n')
my_file.close()

my_file = open("request.txt", "r", encoding="UTF-8")
request = my_file.read()
my_file.close()

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
embeddings = embed(my_string)
test = embed([request])

cos_len = []
for i in embeddings:
    summ = 0
    sum_A = 0
    sum_B = 0
    for j in range(511):
        summ += i[j] * test[0][j]
        sum_A += i[j] ** 2
        sum_B += test[0][j] ** 2
    cos_len.append(float(summ / sqrt(sum_A) * sqrt(sum_B)))
index_max = cos_len.index(max(cos_len))

my_file = open("output.txt", "w", encoding="UTF-8")
my_file.write("Request: " + request + "\n" + my_string[index_max])
my_file.close()
