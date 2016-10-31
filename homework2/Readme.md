# Homework2
### N-gram Model
<br\>
<br\>
Abstract
----------------------------    
This assignment is much related to the N-gram model which we learned in the lecture 6. I show the front process with the vertibi algorithm.      
<br\>
<br\>
Result & Discussion    
----------------------------    
I suffered from the function of the start symbol and the stop symbol. In the unigram model (N = 1), the order of the context isn't considered. As the result, we don't need to add the two symbol to construct the model. On the other hand, the bigram model (N = 2) would consider this relationship. To be notice, the trigram model (N = 3) should add **two** start symbol since we just consider one word in the front. For example, the sentence is ```I love you .``` Since we should consider one word at each time, so we would see the relation toward 'I'. Then the corresponding window is ```[start_symbol, start_symbol, I]```     
<br\>
<p align="center">
  <img src="https://github.com/SunnerLi/pln/blob/master/homework2/img/N-gram_equation.png"/>
</p>
<br\>
The above show the function of the three model. The main concept of the N-gram model is that the specific word is relative to the front N word. The value of N can be change. 1, 2 or 3 are the most common value. The more the value N it is, the more space we should use to store the relation between the windows. As the result, higher gram doesn't been consider in usual.    
<br\>
<br\>
Notice    
---------------------------    
If you're the student of the class, **DONT COPY THE CODE TO GET THE ACCEPTION TOWARD THE CLASS !!!** The purpose of this project is remain the code. Furthermore, it shows for the people who is interested but curious about the meaning of the question.     