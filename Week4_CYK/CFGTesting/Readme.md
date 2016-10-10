# Simple CYK Testing
### Test if it's CFG by Cocke–Younger–Kasami algorithm
<br\>
<br\>
Abstract
----------------------------    
In this code, I show a simple implementation of the cocke-younger-kasami algorithm. This algorithm use dymanic programming idea to solve the problem. By this program, it can determine if the input string corresponds the format of context-free grammar. The time complexity of CYK algorithm is O( n^3 ). 
<br\>
<br\>
Usage
----------------------------    
1. Revise the string you want to test
2. Revise the grammar rule by function ```cnf.rule("S -> AB|BC")```    
3. Run the program and you can see the result    
    
Grammar format    
----------------------------     
The keyin grammar should follow the format:    
(one_non_terminal_symbol)(space)"->"(space)(symbol)"|"(symbol)"|"(symbol)"|"(symbol)    
The following show some valid example:
```
S -> AB|BC
A -> BA|a
B -> CC|b
C -> AB|a
```
<br\>
On the other hands, the following are invalid example:
```
S -> AB | BC    (There cannot insert space between '|' symbol)
S -> A B        (You should use '|' symbol to seperate different symbols)
S ->A           ('->' symbol should concatenate a space)
S->A            (The single space should exist between left symbol and '->' symbol)
```
<br\>
Format Notice    
----------------------------     
1. There're only 2 space near the '->' symbol    
2. Each right symbol split just by '|' symbol    