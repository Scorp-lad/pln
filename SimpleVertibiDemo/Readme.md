# Simple Viterbi Algorithm Demo    
<br/>
Abstract
-----------------------
This program does a simple demo about viterbi algorithm. The part-of-speech (POS) would form the transformation matrix. Second, each candidate word would have various POS. The algorithm would statistic the distribution of each POS of the word. Next, it would compute the transformation probability by sliding toward each training sentences. The viterbi algorithm take greedy method as strategy of the algorithm. It would remain the largest probability to the next concern of the probability.     
<br/>
Notice
-----------------------
This program is just a simple demo. According to some reference, the probability would drop to 0 if the sentence is too long. As the result, we can take logarithm that can make the dropping situation disappear. In this implementation, I don't adopt the logarithm method.    
<br/>
Contain
-----------------------
```
* sentences.txt: the training sentences, there's one sentence in one line
* tag.txt      : the corresponding tag toward the training sentences
* main.py      : the main program
```
<br/>
Modify
-----------------------
You can revise the contain of the variable ```testStr``` in the main.py. However, you should remember the sentence can only composite by the existing word in training data. Otherwise, keyError would occure.    