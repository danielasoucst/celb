from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
# coding: utf-8

def write_tags(fileName,vet):
    file = open(fileName,'w')

    for palavra in vet:
        file.write(palavra.encode('utf-8')+"\n")

    file.close()

def extractFeatures(corpus):
    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer="word", \
                                 tokenizer=None, \
                                 preprocessor=None, \
                                 stop_words=None, \
                                 max_features=1000)
    train_data_features = vectorizer.fit_transform(corpus)
    train_data_features = train_data_features.toarray()
    vocab = vectorizer.get_feature_names()
    write_tags('vocabulario.txt',vocab)

    return train_data_features