# coding: utf-8
import os
import codecs
import pre
import LabeledLineSentence
import arffGenerator as gen
import gensim.models.doc2vec as Doc2Vec
import numpy as np

DIR_BARROCO = './database/barroco/barroco-txt/'
DIR_REALISMO = './database/realismo/realismo-txt/'
DIR_ROMANTISMO = './database/romantismo/romantismo-txt/'

classes = [DIR_BARROCO,DIR_REALISMO]

def createSentence(lista):
    frase = ""
    for l in lista:
        frase += l[0]+" "
    return frase

def createCorpus():
    id=0
    corpus = []
    labels = []
    for classe in classes:
        print("classe",classe)
        file = open('classe'+str(id)+'.txt','w')

        livros = os.listdir(classe)
        for livro in livros:
            f = codecs.open(classe + livro)
            #print (classe + livro)
            raw = f.read().decode("utf-8")
            doc = pre.preProcessarTexto(raw, 10)
            frase = doc.encode("utf-8")
            corpus.append(frase)

            labels.append(id)

            file.write(frase+"\n")
        file.close()
        id+=1
    return corpus,labels

def trainBase():
    train_arrays = []
    train_labels = []

    for i in range(13):
        prefix_train_pos = 'TRAIN_BAR_' + str(i)
        train_arrays.append(model.docvecs[prefix_train_pos])
        train_labels.append(0)

    for j in range(13):
        prefix_train_neg = 'TRAIN_REA_' + str(j)
        train_arrays.append(model.docvecs[prefix_train_neg])
        train_labels.append(1)
    return train_arrays,train_labels



'''MAIN'''
print("Criando corpus")
createCorpus()


sources = {'classe0.txt':'TRAIN_BAR', 'classe1.txt':'TRAIN_REA'}
sentences = LabeledLineSentence.LabeledLineSentence(sources)
model = Doc2Vec.Doc2Vec(min_count=5, window=10, size=300, sample=1e-4, negative=5, workers=8)
model.build_vocab(sentences.to_array())
#print len(model.vocab)
for epoch in range(10):
    model.train(sentences.sentences_perm())
model.save('./imdb.d2v')
print model.most_similar('porque')
#
model = Doc2Vec.Doc2Vec.load('./imdb.d2v')
#print (type(model))
#train_arrays,train_labels = trainBase()
#print (model.docvecs['TRAIN_BAR_0'])
train_arrays, labels_arrays = trainBase()
print train_arrays
print labels_arrays
gen.createArffFile('trainBarrocoRealismoDOC', train_arrays, labels_arrays, len(train_arrays[0]),"{0,1}")

