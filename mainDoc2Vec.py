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
DIR_ARCADISMO = './database/arcadismo/arcadismo-txt/'

classes = [DIR_BARROCO,DIR_ARCADISMO,DIR_REALISMO,DIR_ROMANTISMO]

def createSentence(lista):
    frase = ""
    for l in lista:
        frase += l[0]+" "
    return frase
sizeSample = 50
listQtde = []
def createCorpus():
    id=0
    corpus = []
    labels = []
    for classe in classes:
        print("classe",classe)
        file = open('classe'+str(id)+'.txt','w')
        qtde = 0
        livros = os.listdir(classe)
        for livro in livros:
            f = codecs.open(classe + livro)
            #print (classe + livro)
            raw = f.read().decode("utf-8")
            doc = pre.preProcessarTexto(raw, 10)
            if(len(doc)>sizeSample):
                for k in range (0,sizeSample):
                    qtde+=1
                    frase = doc[k].encode("utf-8")
                    corpus.append(frase)
                    labels.append(id)

                    file.write(frase+"\n")
            else:
                for k in range (0,len(doc)):
                    qtde+=1
                    frase = doc[k].encode("utf-8")
                    corpus.append(frase)
                    labels.append(id)

                    file.write(frase+"\n")
        file.close()
        listQtde.append(qtde)
        id+=1
    return corpus,labels

def trainBase():
    train_arrays = []
    train_labels = []

    for i in range(listQtde[0]):
        prefix_train_pos = 'TRAIN_BAR_' + str(i)
        train_arrays.append(model.docvecs[prefix_train_pos])
        train_labels.append(0)
    for l in range(listQtde[1]):
        prefix_train_pos = 'TRAIN_ARC_' + str(l)
        train_arrays.append(model.docvecs[prefix_train_pos])
        train_labels.append(1)

    for j in range(listQtde[2]):
        prefix_train_neg = 'TRAIN_REA_' + str(j)
        train_arrays.append(model.docvecs[prefix_train_neg])
        train_labels.append(2)
    for k in range(listQtde[3]):
        prefix_train_neg = 'TRAIN_ROM_' + str(k)
        train_arrays.append(model.docvecs[prefix_train_neg])
        train_labels.append(3)
    return train_arrays,train_labels



'''MAIN'''
print("Criando corpus")
createCorpus()
print listQtde

sources = {'classe0.txt':'TRAIN_BAR','classe1.txt':'TRAIN_ARC', 'classe2.txt':'TRAIN_REA','classe3.txt':'TRAIN_ROM'}
sentences = LabeledLineSentence.LabeledLineSentence(sources)
model = Doc2Vec.Doc2Vec(min_count=5, window=10, size=100, sample=1e-4, negative=5, workers=8)
#model = Doc2Vec.Doc2Vec(alpha=0.025, min_alpha=0.025)
model.build_vocab(sentences.to_array())
#print len(model.vocab)
for epoch in range(10):
    model.train(sentences.sentences_perm())
model.save('./imdb.d2v')
# print model.most_similar('porque')
#
model = Doc2Vec.Doc2Vec.load('./imdb.d2v')
#print (type(model))
#train_arrays,train_labels = trainBase()
#print (model.docvecs['TRAIN_BAR_0'])
train_arrays, labels_arrays = trainBase()

print("Gerando arquivo arff")
gen.createArffFile('barReaRomArcDOC', train_arrays, labels_arrays, len(train_arrays[0]),"{0,1,2,3}")
