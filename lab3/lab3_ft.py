from gensim.models.fasttext import FastText
from gensim.test.utils import datapath
from gensim import utils


# Set file names for train and test data
# corpus_file = datapath('merged_clean.txt')

class MyCorpus:
    """An iterator that yields sentences (lists of str)."""

    def __iter__(self):
        corpus_path = open("merged_clean.txt", "r", encoding="UTF-8")
        for line in (corpus_path):
            # assume there's one document per line, tokens separated by whitespace
            yield utils.simple_preprocess(line)


sentences = MyCorpus()

model = FastText(sentences, vector_size=160)

# # build the vocabulary
# model.build_vocab(corpus_file=corpus_file)
#
# # train the model
# model.train(
#     corpus_file=corpus_file, epochs=model.epochs,
#     total_examples=model.corpus_count, total_words=model.corpus_total_words,)


output = (model.wv.most_similar(['dog'], ['small'], topn=5))

my_file = open("output_ft.txt", "w", encoding="UTF-8")
my_file.write(str(output))
my_file.close()
