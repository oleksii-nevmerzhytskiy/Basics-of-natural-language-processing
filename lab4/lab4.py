import re
from nltk.stem import PorterStemmer
from nltk.tokenize import MWETokenizer
from sklearn import metrics
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import csv


def non_letter(str):
    return re.sub("[0-9\W_]", " ", str)


def tokenization(str):
    tokenizer = MWETokenizer()
    return tokenizer.tokenize(str.split())


def stemmer_list(word_list):
    stemmer = PorterStemmer()
    stemmer_word_list = [stemmer.stem(word) for word in word_list]
    return stemmer_word_list


my_file = open("moviereviews_100.tsv", "r", encoding="UTF-8")
my_string = my_file.read().split('"\nneg	"')
my_file.close()
q = [w for w in my_string if w != '']
for i in range(len(q)):
    q[i] = non_letter(q[i])
    q[i] = tokenization(q[i])
    q[i] = stemmer_list(q[i])

dct = Dictionary(q)  # fit dictionary
corpus = [dct.doc2bow(line) for line in q]  # convert corpus to BoW format
model = TfidfModel(corpus)  # fit model

arrayX = []
arrayY = []
arrayZ = []

for j in range(len(corpus)):
    vector = model[corpus[j]]
    for i in range(len(vector)):
        arrayX.append(vector[i][0])
        arrayY.append(vector[i][1])
        arrayZ.append(j)

data = pd.DataFrame({
    'x': arrayX,
    'y': arrayY,
    'z': arrayZ
})

X = data[['x', 'y', 'z']]
y = data['z']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

d = (pd.DataFrame.to_dict(X_test))
dy = (d['y'])

with open('output.csv', mode='w') as csv_file:
    fieldnames = ['word id', 'vector', 'text id']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    j = 0
    for i in dy:
        writer.writerow({'word id': str(i), 'vector': str(dy[i]), 'text id': str(y_pred[j])})
        j += 1

accuracy = (metrics.accuracy_score(y_test, y_pred))
precision = (metrics.precision_score(y_test, y_pred, average='macro'))
recall = (metrics.recall_score(y_test, y_pred, average='macro'))
matthews_Correlation_Coefficient = (metrics.matthews_corrcoef(y_test, y_pred))

my_file = open("metrics.txt", "w", encoding="UTF-8")
my_file.write("Accuracy: " + str(accuracy)
              + '\nPrecision: ' + str(precision)
              + '\nRecall: ' + str(recall)
              + '\nMatthews Correlation Coefficient: ' + str(matthews_Correlation_Coefficient))
my_file.close()
