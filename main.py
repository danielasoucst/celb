# coding: utf-8
import sys
import string
import os
import codecs
import preprocessamento as pre
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

DIR_BARROCO = './database/barroco/barroco-txt/'

'''dir = '/home/daniela/PycharmProjects/celb/database/barroco/bizarro.txt'
f = codecs.open(dir)
raw = f.read().decode("utf-8")
for r in raw:
    if(r == ''):
        print('bizarroo')
    print(r)'''

def juntarPalavras(lista):
    frase = ""
    for l in lista:
        frase += l[0]+" "
    return frase

livros = os.listdir(DIR_BARROCO)
corpus = []
for livro in livros:
    f = codecs.open(DIR_BARROCO+livro)
    raw = f.read().decode("utf-8")
    listaResultante = pre.preProcessarTexto(raw, 10)
    print(listaResultante)
    corpus.append(juntarPalavras(listaResultante))

arq = open('vamo.txt','w')
for p in corpus:
    arq.write(p+"\n")
arq.close()
# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000)
train_data_features = vectorizer.fit_transform(corpus)
train_data_features = train_data_features.toarray()
print("BAG")
print train_data_features
print train_data_features.shape
vocab = vectorizer.get_feature_names()
print vocab
# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features, axis=0)

# For each, print the vocabulary word and the number of times it
# appears in the training set
for tag, count in zip(vocab, dist):
    print count, tag


#https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words





'''vectorizer = CountVectorizer(analyzer = "word", tokenizer = None,preprocessor = None, stop_words = None, max_features = 5000)
train_data_features = vectorizer.fit_transform(listaResultante)
train_data_features = train_data_features.toarray()
print (train_data_features)'''