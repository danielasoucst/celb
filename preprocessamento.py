# coding: utf-8
import nltk
import string
import sys

def transMinusculo(tokens):
    return [w.lower() for w in tokens]

def delPontuacao(palavras):
    punctuations = string.punctuation
    list = []
    for i in palavras:
        if (i not in punctuations):
            list.append(i)
    return list

def delStopWords(palavras):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    stopwords.append('www.nead.unama.br')
    lstSemStop = []

    for l in palavras:
        if (l not in stopwords):
            lstSemStop.append(l)

    return lstSemStop


def preProcessarTexto(txt,qtdeTermos):

    tokens = nltk.word_tokenize(txt)
    words = transMinusculo(tokens)

    lstSemPont = delPontuacao(words)
    lstSemStop = delStopWords(lstSemPont)

    fd = nltk.FreqDist(lstSemStop)
    return fd.most_common(qtdeTermos)
   # return lstSemStop


