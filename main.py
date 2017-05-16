# coding: utf-8
import sys
import string
import os
import codecs
import preprocessamento as pre
import extratorcaracteristicas as ext
import arffGenerator as gen

DIR_BARROCO = './database/barroco/barroco-txt/'
DIR_REALISMO = './database/realismo/realismo-txt/'
DIR_ROMANTISMO = './database/romantismo/romantismo-txt/'

def createSentence(lista):
    frase = ""
    for l in lista:
        frase += l[0]+" "
    return frase

def createCorpus():
    livros = os.listdir(DIR_ROMANTISMO)
    qtdeLivrosBarroco = len(livros)
    livros += os.listdir(DIR_REALISMO)
    corpus = []
    k = 0
    vetLabels = []
    for livro in livros:
        if(k<qtdeLivrosBarroco):
            f = codecs.open(DIR_ROMANTISMO+livro)
            vetLabels.append(0)
        else:
            if(k >= 2*qtdeLivrosBarroco):
                break
            f = codecs.open(DIR_REALISMO + livro)
            vetLabels.append(1)
        raw = f.read().decode("utf-8")
        listaResultante = pre.preProcessarTexto(raw, 10)
        #print(listaResultante)
        corpus.append(createSentence(listaResultante))
        k += 1

    return [corpus,vetLabels]


'''Main'''
print("Criando corpus")
corpus = createCorpus()
if(corpus!=None):
    print("Extraindo características")
    features = ext.extractFeatures(corpus[0])
    ''''print corpus[1]
    print(features.shape)
    print(features)
    print("Gerando arquivo arff")
    gen.createArffFile('trainBarrocoRealismo',features,corpus[1],features.shape[1])'''

