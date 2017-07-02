'''
Sistemas Inteligentes
Alunos: Daniela e Anderson
Descrição: main.py => extrai características com BOW
mainDoC2Vec => extrai características com doc2vec
'''

# coding: utf-8
import os
import codecs
import preprocessamento as pre
import extratorcaracteristicas as ext
import arffGenerator as gen



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

def createCorpus():
    id = 0
    labels = []
    corpus = []
    for classe in classes:
        print("classe", classe)
        file = open('classe' + str(id) + '.txt', 'w')
        if(file!=None): print ("criou arquivo...")
        livros = os.listdir(classe)
        for livro in livros:
            f = codecs.open(classe + livro)
            labels.append(id)
            # print (classe + livro)
            raw = f.read().decode("utf-8")

            listaResultante = pre.preProcessarTexto(raw, 20)
            # #print(listaResultante)

            frase = createSentence(listaResultante)
            corpus.append(frase)
            frase = frase.encode("utf-8")

            # k += 10
            file.write(frase + "\n")
        file.close()
        id += 1
    return corpus,labels

import nltk


'''Main'''
print("Criando corpus")
corpus,labels = createCorpus()
print (len(corpus),len(labels))


if(labels!=None):
    print("Extraindo características pra treino")
    features = ext.extractFeatures(corpus)
    print(features.shape)
    #print("Gerando arquivo arff")
    gen.createArffFile('./testes/barReaRomArc',features,labels,features.shape[1],"{0,1,2,3}")

