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
    mat = []

    for i in range(0,len(lstSemStop),100):

        # print i,len(lstSemStop)/100
        # part = lstSemStop[i:i + 100]
        # print len(part)
        part = lstSemStop[i:i + 100]
        doc = ""
        for w in part:
            doc += w
            doc += " "
        mat.append(doc)



    # fd = nltk.FreqDist(lstSemStop)
    # print(fd.most_common(qtdeTermos))

    return mat


