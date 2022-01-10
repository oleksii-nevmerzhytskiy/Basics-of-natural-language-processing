from gensim import utils
import gensim.models


class MyCorpus:
    """An iterator that yields sentences (lists of str)."""

    def __iter__(self):
        corpus_path = open("merged_clean.txt", "r", encoding="UTF-8")
        for line in (corpus_path):
            # assume there's one document per line, tokens separated by whitespace
            yield utils.simple_preprocess(line)


sentences = MyCorpus()
model = gensim.models.Word2Vec(sentences, vector_size=320)

output = model.wv.most_similar(['dog'], ['orange'], topn=5)
my_file = open("output_w2v.txt", "w", encoding="UTF-8")
my_file.write(str(output))
my_file.close()
