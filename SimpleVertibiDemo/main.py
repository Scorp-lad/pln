from collections import Counter
from collections import defaultdict
from viterbi import Viterbi

strings = []                    # List of the word list
tags = []                       # List of the POS list
tagTypes = set()                # List of the whole possible POS

word_pos_prob = dict()          # The probability of the specific word with the specific POS
pos_pos_prob  = defaultdict()   # The probability of the POS transferring
pos_prob = dict()               # The probability of POS distribution

def load():
    """
        Load the whole sentences and the corresponding POS
    """
    global strings
    global tags
    global tagTypes

    with open('sentences.txt', 'r') as f:
        for sentence in f.readlines():
            strings.append(sentence.split())
    with open('tag.txt', 'r') as f:
        for sentence in f.readlines():
            tags.append(sentence.split())
    for i in tags:
        for j in i:
            tagTypes.add(j)
    tagTypes = list(tagTypes)

def getWordPOSProbability():
    """
        Statistic the probability of the word with the specific POS
    """
    global word_pos_prob
    word_freq = []              # The frequency of each word
    word_pos  = []              # The existing pair about word and POS
    word_pos_freq = None        # The frequency of each possible pair
    
    # Get the frequency of each word
    for sentence in strings:
        for word in sentence:
            word_freq.append(word)
    word_freq = Counter(word_freq)

    # Get the frequency of the each word with the corresponding POS
    for i in xrange(len(strings)):
        for j in xrange(len(strings[i])):
            word_pos.append((strings[i][j], tags[i][j]))
    word_pos_freq = Counter(word_pos)

    # Get the probability of each word with corresponding POS
    for tag in tagTypes:
        for word in word_freq:
            word_pos_prob[(word, tag)] = float(word_pos_freq[(word, tag)]) / word_freq[word]

def getPOSTransformProbability():
    """
        Statistic the transformation probability of POS
        Notice: The frequency statistic doesn't include the last tag in each sentence
    """
    global pos_pos_prob
    pos_freq = []               # The frequency of each prefix POS
    pos_pos  = []               # The existing pair about POS and POS
    pos_pos_freq = None         # The frequency of each possible POS pair

    # Get the whole prefix POS pair and the frequency of each POS
    for sentence in tags:
        for i in range(len(sentence)-1):
            pos_pos.append((sentence[i], sentence[i+1]))
            pos_freq.append(sentence[i])
    pos_freq = Counter(pos_freq)
    pos_pos_freq = Counter(pos_pos)

    # Get the POS transform probability
    for tag1 in tagTypes:
        for tag2 in tagTypes:
            try:
                pos_pos_prob[(tag1, tag2)] = float(pos_pos_freq[(tag1, tag2)]) / pos_freq[tag1]
            except:
                pos_pos_prob[(tag1, tag2)] = 0.0

def getPOSDistributionProbability():
    """
        Statistic the distribution probability of POS 
        This result would include the last tag in each sentence
    """
    global pos_prob

    # Get the POS distribution
    pos_prob = defaultdict(lambda: 0)
    for sentence in tags:
        for tag in sentence:
            pos_prob[tag] += 1
    
    # Normalize
    sum = 0
    for pair in pos_prob.items():
        sum += pair[1]
    for key in pos_prob:
        pos_prob[key] = float(pos_prob[key]) / sum

if __name__ == "__main__":
    # Load the statistic information
    load()
    getWordPOSProbability()
    getPOSTransformProbability()
    getPOSDistributionProbability()

    # Testing
    # The sentence "I love NTPU" doesn't in the training set
    # However, the algorithm can predict the correct POS
    v = Viterbi(word_pos_prob, pos_pos_prob, pos_prob, tagTypes)
    testStr = "I love NTPU"
    print "Sentence   : ", testStr
    print "POS predict: ", v.work(testStr)