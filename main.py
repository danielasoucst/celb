# coding: utf-8
import sys
import string
import os
import codecs
import preprocessamento as pre


DIR_BARROCO = './database/barroco/barroco-txt/'


livros = os.listdir(DIR_BARROCO)
for livro in livros:
    f = codecs.open(DIR_BARROCO+livro)
    raw = f.read().decode("utf-8")
    listaResultante = pre.preProcessarTexto(raw, 10)


#https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words





'''vectorizer = CountVectorizer(analyzer = "word", tokenizer = None,preprocessor = None, stop_words = None, max_features = 5000)
train_data_features = vectorizer.fit_transform(listaResultante)
train_data_features = train_data_features.toarray()
print (train_data_features)'''