# Homework1
### Dependency parsing
<br\>
<br\>
Abstract
----------------------------    
The parsing problem is the most popular problem in NLP. From 1990s, there're many algorithm that try to optimize. The CYK-like algorithm is the first method to reach the goal. Nevertheless, the complexity is big O( n^5 ). In this homework, I follow the tutorial and use CoNLL dataset to train SVM model. Next, This code complete the parsing task by the Nivre's arc-eager transition-based dependency parser. At last, I follow the request to create the parser.py that would show the dependency relationship.    
<br\>
<br\>
Result & Discussion    
----------------------------    
At first, I modify the shift and reduce transition. This is the first I try to modify the other's python code. Luckily, the tutorial is very detailed that I didn't waste a lot of time to get the point. For the most important, the Nivre algorithm would use the auxiliary stack to reduce the complexity that the stack might get empty. During the implementation, you should be careful to prevent the stack empty.    
<br\>
At Second part, The question request to add the additional features to enhence the LAS score. First, I try to detect and append the attribute tags which are shown in the external publication. However, I found the LAS score might not raise after the notification. Not the whole feature you add would improve the result. Afterward, I try to append the tags which the token really has. By the inspection, I get the higher score though.    
<br\>
The complexity of the Nivre algorithm is big O( n ). It is a big improvement rather than the CYK-like algorithm. On the contrary, Each word would be processed once. By the specification, this algorithm cannot deal with the non-projective problem.    
<br\>
<br\>
Contain    
---------------------------    
```
* trainAll.py - train the whole three model at one time    
* test.py     - the evaluation code
* parser.py   - show the dependency for the specific sentence
```
<br\>
<br\>
Usage    
---------------------------    
1. Decompress the training data and testing data: ```unzip data.zip```
2. Run the code: ```python test.py```
<br\>
<br\>

Notice    
---------------------------    
If you're the student of the class, **DONT COPY THE CODE TO GET THE ACCEPTION TOWARD THE CLASS !!!** The purpose of this project is remain the code. Furthermore, it shows for the people who is interested but curious about the meaning of the question.     