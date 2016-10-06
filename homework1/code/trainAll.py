import random
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition

if __name__ == '__main__':
    random.seed(1234)

    # Tain the english model
    print "--->\t Load the english corpus"
    data = dataset.get_english_train_corpus().parsed_sents()
    #data = dataset.get_english_test_corpus().parsed_sents()
    tp = TransitionParser(Transition, FeatureExtractor)
    subdata = random.sample(data, 200)
    #subdata = data
    print "--->\t Train english corpus model"
    tp.train(subdata)
    tp.save('english.model')

    # Tain the danish model
    print "--->\t Load the danish corpus"
    data = dataset.get_danish_train_corpus().parsed_sents()
    #data = dataset.get_danish_test_corpus().parsed_sents()
    tp = TransitionParser(Transition, FeatureExtractor)
    subdata = random.sample(data, 200)
    #subdata = data
    print "--->\t Train danish corpus model"
    tp.train(subdata)
    tp.save('danish.model')

    # Tain the swedish model
    print "--->\t Load the swedish corpus"
    data = dataset.get_swedish_train_corpus().parsed_sents()
    #data = dataset.get_swedish_test_corpus().parsed_sents()
    tp = TransitionParser(Transition, FeatureExtractor)
    subdata = random.sample(data, 200)
    #subdata = data
    print "--->\t Train swedish corpus model"
    tp.train(subdata)
    tp.save('swedish.model')