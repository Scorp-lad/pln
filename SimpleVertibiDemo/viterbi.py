from collections import Counter
from collections import defaultdict

class Viterbi(object):
    def __init__(self, outputMatrix, transformMatrix, posDistribution, posList):
        self.__outputMatrix = outputMatrix
        self.__transformMatrix = transformMatrix
        self.__posDistribution = posDistribution
        self.__posList = posList

    def work(self, testString):
        """
            Implement viterbi algorithm

            Arg:    The string which want to predict the corresponding POS
            Ret:    The predict POS list
        """
        # Initialize
        testString = testString.split()
        probabilities = [1] * len(self.__posList)
        for i in range(len(probabilities)):
            probabilities[i] = self.__posDistribution[self.__posList[i]]

        # First state
        res = []
        for i in range(len(probabilities)):
            probabilities[i] *= self.__outputMatrix[testString[0], self.__posList[i]]
        res.append(self.__posList[ probabilities.index(max(probabilities)) ])

        # Viterbi
        for i in range(1, len(testString)):
            _probabilities = []
            for j in range(len(probabilities)):
                __probabilities = []
                for k in range(len(probabilities)):
                    __probability = probabilities[k] * \
                        self.__transformMatrix[(self.__posList[k], self.__posList[j])] * \
                        self.__outputMatrix[testString[i], self.__posList[j]]
                    __probabilities.append(__probability)
                _probabilities.append(max(__probabilities))
            for j in range(len(probabilities)):
                probabilities[j] = _probabilities[j]
            res.append( self.__posList[_probabilities.index(max(_probabilities))] )
        return res

if __name__ == "__main__":
    v = Viterbi(dict(), defaultdict())