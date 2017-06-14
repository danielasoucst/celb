# gensim modules
import gensim.utils as  utils
import gensim.models.doc2vec as LabeledSentence
from gensim.models import Doc2Vec

# numpy
import numpy

# random
from random import shuffle

# classifier
# from sklearn.linear_model import LogisticRegression

class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources

        flipped = {}
        print ("mar oi")
        # make sure that keys are unique
        for key, value in sources.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                raise Exception('Non-unique prefix encountered')

    def __iter__(self):
        print ("mar oi2")
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    # print ("aa",prefix + '_%s' % item_no)
                    yield LabeledSentence.LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no])

    def to_array(self):
        self.sentences = []
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    # print ("e",prefix + '_%s' % item_no)
                    self.sentences.append(LabeledSentence.LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no]))
        for s in self.sentences:
            print s
        return self.sentences

    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences