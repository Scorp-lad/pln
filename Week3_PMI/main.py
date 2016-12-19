"""
    This program would measure the association strength
"""
from collections import Counter
import math

# Laplace parameter
lap_k = 1

def PMI(string1, string2):
    """
        Return the value of pointwise nutual information

        Arg:    string1 - The first word you want to measure
                string2 - The second word you want to measure
        Ret:    The value of PMI
    """
    wordBag = set()                     # Help to do the laplace smoothing
    sentences = None                    # Store the sentences contained in the corpus
    with open('train.dat', 'r') as f:
        sentences = f.readlines()
    occurenceString1 = 0.0
    occurenceString2 = 0.0
    occurenceBoth = 0.0

    # Get the probability by the maximun likelihood estimation
    for sentence in sentences:
        sentence = Counter(sentence.split())
        if string1 in sentence:
            occurenceString1 += sentence[string1]
        if string2 in sentence:
            occurenceString2 += sentence[string2]
            if string1 in sentence:
                occurenceBoth += min(sentence[string1], sentence[string2])
        for word in sentence:
            wordBag.add(word)
    
    # Return the result (the laplace smoothing would be done if divide by zero)
    try:
        return math.log(occurenceBoth) / ( math.log(occurenceString1) * math.log(occurenceString2) )
    except:
        return laplaceSmoothing(math.log(occurenceBoth), math.log(occurenceString1), math.log(occurenceString2), wordBag)

def laplaceSmoothing(up, down1, down2, wordBag):
    """
        Do the Laplace smoothing for the calculation of probability
        The formula is:           count(word) + lap_k
                            _________________________________
                              N + lap_k*count(type_of word)

        Arg:    up      - log(v, w)
                down1   - log(v)
                down2   - log(w)
                wordBag - The number of different type words
        Ret:    The probability value after the process of laplace smoothing
    """
    return (up + lap_k) / (down1*down2 + len(wordBag)*lap_k)

if __name__ == "__main__":
    print "PMI(apple, fruit): ", PMI("apple", "fruit")
