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
    stopwords.append(u'ff')#quadrado estranho
    stopwords.append(u'\u2014')#underline estranho
    stopwords.append('\xe2\x80\x94')
    stopwords.append(u'f\xe9')
    lstSemStop = []

    for l in palavras:
        l = l.encode("utf-8")
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


