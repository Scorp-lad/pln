from collections import defaultdict
import collections
import math
import nltk
import time

# Constants to be used by you when you fill the functions
START_SYMBOL = '*'
STOP_SYMBOL = 'STOP'
MINUS_INFINITY_SENTENCE_LOG_PROB = -1000

# TODO: IMPLEMENT THIS FUNCTION
# Calculates unigram, bigram, and trigram probabilities given a training corpus
# training_corpus: is a list of the sentences. Each sentence is a string with tokens separated by spaces, ending in a newline character.
# This function outputs three python dictionaries, where the keys are tuples expressing the ngram and the value is the log probability of that ngram
def calc_probabilities(training_corpus):
    unigram_p = {}
    bigram_p = {}
    trigram_p = {}
    
    # Deal with unigram
    wordNum = 0
    counting = defaultdict(lambda: 0)
    for sentence in training_corpus:
        sentence = sentence + ' ' + STOP_SYMBOL
        tokens = sentence.split()
        wordNum += (len(tokens))
        for item in tokens:
            counting[(item,)] += 1
    for word in counting:
        unigram_p[word] = math.log(float(counting[word]) / wordNum) / math.log(2)
    print wordNum
    print counting[("captain",)]
    print unigram_p[("captain",)]

    # Deal with bigram
    biCounting = defaultdict(lambda: 0)
    counting[(START_SYMBOL, )] = len(training_corpus)
    for sentence in training_corpus:
        sentence = START_SYMBOL + ' ' + sentence + ' ' + STOP_SYMBOL
        tokens = sentence.split()
        for i in range(len(tokens)-1):
            biCounting[(tokens[i], tokens[i+1])] += 1
    for key in biCounting:
        bigram_p[key] = math.log(float(biCounting[key]) / counting[(key[0],)]) / math.log(2)
    print bigram_p[('and', 'religion')]

    # Deal with trigram
    triCounting = defaultdict(lambda: 0)
    biCounting[(START_SYMBOL, START_SYMBOL)] = len(training_corpus)
    for sentence in training_corpus:
        sentence = START_SYMBOL + ' ' + START_SYMBOL + ' ' + sentence + ' ' + STOP_SYMBOL
        tokens = sentence.split()
        for i in range(len(tokens)-2):
            triCounting[(tokens[i], tokens[i+1], tokens[i+2])] += 1
    for key in triCounting:
        trigram_p[key] = math.log(float(triCounting[key]) / biCounting[(key[0], key[1])]) / math.log(2)
    print trigram_p[('and', 'not', 'come')]
    
    return unigram_p, bigram_p, trigram_p

# Prints the output for q1
# Each input is a python dictionary where keys are a tuple expressing the ngram, and the value is the log probability of that ngram
def q1_output(unigrams, bigrams, trigrams, filename):
    # output probabilities
    outfile = open(filename, 'w')

    unigrams_keys = unigrams.keys()
    unigrams_keys.sort()
    for unigram in unigrams_keys:
        outfile.write('UNIGRAM ' + unigram[0] + ' ' + str(unigrams[unigram]) + '\n')

    bigrams_keys = bigrams.keys()
    bigrams_keys.sort()
    for bigram in bigrams_keys:
        outfile.write('BIGRAM ' + bigram[0] + ' ' + bigram[1]  + ' ' + str(bigrams[bigram]) + '\n')

    trigrams_keys = trigrams.keys()
    trigrams_keys.sort()    
    for trigram in trigrams_keys:
        outfile.write('TRIGRAM ' + trigram[0] + ' ' + trigram[1] + ' ' + trigram[2] + ' ' + str(trigrams[trigram]) + '\n')

    outfile.close()


# TODO: IMPLEMENT THIS FUNCTION
# Calculates scores (log probabilities) for every sentence
# ngram_p: python dictionary of probabilities of uni-, bi- and trigrams.
# n: size of the ngram you want to use to compute probabilities
# corpus: list of sentences to score. Each sentence is a string with tokens separated by spaces, ending in a newline character.
# This function must return a python list of scores, where the first element is the score of the first sentence, etc. 
def score(ngram_p, n, corpus):
    scores = []
    
    for sentence in corpus:
        # Initialize
        key = None
        pr = 0.0

        # Recover the sentence
        sentence = sentence.split()
        if n == 1   :   sentence = sentence + [STOP_SYMBOL]
        if n == 2   :   sentence = [START_SYMBOL] + sentence + [STOP_SYMBOL]
        if n == 3   :   sentence = [START_SYMBOL] + [START_SYMBOL] + sentence + [STOP_SYMBOL]
        
        # Scanning for the whole sentence
        for i in range(len(sentence) - n + 1):
            # Find the key
            if n == 1   :   key = (sentence[i], )
            if n == 2   :   key = (sentence[i], sentence[i+1])
            if n == 3   :   key = (sentence[i], sentence[i+1], sentence[i+2])

            # Multiple the probability
            try:
                pr += ngram_p[key]
            except ValueError:
                pr = MINUS_INFINITY_SENTENCE_LOG_PROB
                break
        scores.append(pr)

    return scores

# Outputs a score to a file
# scores: list of scores
# filename: is the output file name
def score_output(scores, filename):
    outfile = open(filename, 'w')
    for score in scores:
        outfile.write(str(score) + '\n')
    outfile.close()

# TODO: IMPLEMENT THIS FUNCTION
# Calculates scores (log probabilities) for every sentence with a linearly interpolated model
# Each ngram argument is a python dictionary where the keys are tuples that express an ngram and the value is the log probability of that ngram
# Like score(), this function returns a python list of scores
def linearscore(unigrams, bigrams, trigrams, corpus):
    scores = []
    
    for sentence in corpus:
        pr = 0

        # Recover the sentence
        sentence = sentence.split()
        sentence = [START_SYMBOL] + [START_SYMBOL] + sentence + [STOP_SYMBOL]

        # Scanning for the whole sentence
        for i in range(len(sentence) - 2):
            key_u = (sentence[i+2], )
            key_b = (sentence[i+1], sentence[i+2])
            key_t = (sentence[i], sentence[i+1], sentence[i+2])

            try:
                pr_u = pow(2, unigrams[key_u])
            except KeyError:
                pr_u = pow(2, MINUS_INFINITY_SENTENCE_LOG_PROB)
            try:
                pr_b = pow(2, bigrams[key_b])
            except KeyError:
                pr_b = pow(2, MINUS_INFINITY_SENTENCE_LOG_PROB)
            try:
                pr_t = pow(2, trigrams[key_t])
            except KeyError:
                pr_t = pow(2, MINUS_INFINITY_SENTENCE_LOG_PROB)

            pr += math.log((pr_u + pr_b + pr_t)/3) / math.log(2)

        # Append the score
        scores.append(pr)

    return scores

DATA_PATH = 'data/'
OUTPUT_PATH = 'output/'

# DO NOT MODIFY THE MAIN FUNCTION
def main():
    # start timer
    time.clock()

    # get data
    infile = open(DATA_PATH + 'Brown_train.txt', 'r')
    corpus = infile.readlines()
    infile.close()

    # calculate ngram probabilities (question 1)
    unigrams, bigrams, trigrams = calc_probabilities(corpus)

    # question 1 output
    q1_output(unigrams, bigrams, trigrams, OUTPUT_PATH + 'A1.txt')

    # score sentences (question 2)
    uniscores = score(unigrams, 1, corpus)
    biscores = score(bigrams, 2, corpus)
    triscores = score(trigrams, 3, corpus)

    # question 2 output
    score_output(uniscores, OUTPUT_PATH + 'A2.uni.txt')
    score_output(biscores, OUTPUT_PATH + 'A2.bi.txt')
    score_output(triscores, OUTPUT_PATH + 'A2.tri.txt')

    # linear interpolation (question 3)
    linearscores = linearscore(unigrams, bigrams, trigrams, corpus)

    # question 3 output
    score_output(linearscores, OUTPUT_PATH + 'A3.txt')

    # open Sample1 and Sample2 (question 5)
    infile = open(DATA_PATH + 'Sample1.txt', 'r')
    sample1 = infile.readlines()
    infile.close()
    infile = open(DATA_PATH + 'Sample2.txt', 'r')
    sample2 = infile.readlines()
    infile.close() 

    # score the samples
    sample1scores = linearscore(unigrams, bigrams, trigrams, sample1)
    sample2scores = linearscore(unigrams, bigrams, trigrams, sample2)

    # question 5 output
    score_output(sample1scores, OUTPUT_PATH + 'Sample1_scored.txt')
    score_output(sample2scores, OUTPUT_PATH + 'Sample2_scored.txt')

    # print total time to run Part A
    print "Part A time: " + str(time.clock()) + ' sec'

if __name__ == "__main__": main()
