# coding: utf-8
import nltk
import string
import chardet
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

def delStopWords(palavras): #AS comparações de string são feitas em unicode
    stopwords = nltk.corpus.stopwords.words('portuguese')
    lstSemStop = []

    stopwords.append(u'www.nead.unama.br')
    stopwords.append(u'...')
    stopwords.append(u'!...')
    stopwords.append(u'?...')
    stopwords.append(u'é')
    stopwords.append(u'``')
    stopwords.append(u"''")
    stopwords.append(u'—')
    stopwords.append(u'ff')
    stopwords.append(u'--')

    for l in palavras:
        l = l.encode("utf-8")
        l = unicode(l, "utf-8")
        if (l not in stopwords):
            lstSemStop.append(l)

    return lstSemStop


def preProcessarTexto(txt,qtdeTermos):

    tokens = nltk.word_tokenize(txt)
    words = transMinusculo(tokens)

    lstSemPont = delPontuacao(words)
    lstSemStop = delStopWords(lstSemPont)
    '''for t in lstSemStop:
        print t'''
    fd = nltk.FreqDist(lstSemStop)
    return fd.most_common(qtdeTermos)
   # return lstSemStop


