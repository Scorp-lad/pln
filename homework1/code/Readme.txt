part 1:
After I complete the four transitor, I got the result:
UAS: 0.144791874129 
LAS: 0.0649273053177

part 2:
At first, I modify the shift and reduce transition. 
This is the first I try to modify the other's python code. 
Luckily, the tutorial is very detailed that I didn't waste a lot of time to get the point. 
For the most important, the Nivre algorithm would use the auxiliary stack to reduce the complexity that the stack might get empty. 
During the implementation, you should be careful to prevent the stack empty.
At Second part, The question request to add the additional features to enhence the LAS score. 
First, I try to detect and append the attribute tags which are shown in the external publication. 
However, I found the LAS score might not raise after the notification. 
Not the whole feature you add would improve the result. 
Afterward, I try to append the tags which the token really has. 
By the inspection, I get the higher score though.
The complexity of the Nivre algorithm is big O( n ). It is a big improvement rather than the CYK-like algorithm. 
On the contrary, Each word would be processed once. 
By the specification, this algorithm cannot deal with the non-projective problem.