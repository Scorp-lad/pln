from eigenDemo import *
from svd import *

"""
    Demo program

    The IMG(0) is the variable of input matrix
"""
read()
a_, u, s, v = SVD(IMG(0), discard=2, reduction=False)
print "origin: ", IMG(0)
print ""
print "reduce: ", a_
print ""