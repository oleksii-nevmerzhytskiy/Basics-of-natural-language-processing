from gensim.corpora import Dictionary

my_file = open("output.txt", "r", encoding="UTF-8")
my_string = my_file.read()
my_file.close()

my_string = my_string.split()
texts = [my_string]
print(texts)
dct = Dictionary(texts)  # initialize a Dictionary
print(dct)
print(dct.doc2idx(["автор"]))