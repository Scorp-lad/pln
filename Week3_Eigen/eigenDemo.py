from scipy import linalg as la
import numpy as np
import os

_arr = []
vals = []
vecs = []

IMG = lambda x: _arr if _arr == None else _arr

def read(fileName="mat.txt"):
    """
        Read the matrix from file
    """
    global _arr 

    # Read the contain
    f = open(fileName, 'r')
    while True:
        rowString = f.readline()
        rowString = rowString[:len(rowString)-1]
        if not rowString:
            break
        rowString = str(rowString).split(' ')
        _arr.append(rowString) 
    
    # Check if valid
    length = len(_arr[0])
    for i in _arr:
        if len(i) != length:
            print "invalid matrix!"
            return None

    # Change to numpy object
    for i in range(len(_arr)):
        for j in range(len(_arr[0])):
            _arr[i][j] = int(_arr[i][j])
    return np.asarray(_arr)

def write(fileName="mat.txt"):
    """
        Write the result to the file
    """
    global _arr, vals, vecs
    f = open(fileName, 'w')

    # Write the origin
    for i in range(len(_arr)):
        for j in range(len(_arr[0])):
            f.write(str(_arr[i][j]))
            if not j == len(_arr[0])-1:
                f.write(" ")
            else:
                f.write("\n")

    # Write the eigen value matrix
    print vals
    f.write("\n\nEigen value matrix: \n")
    for i in range(len(vals)):
        f.write(str(vals[i]))
        f.write("\t")
    f.write("\n")

    # Write the eigen vector matrix
    f.write("\n\nEigen vector matrix: \n")
    for i in range(len(vecs)):
        for j in range(len(vecs[0])):
            f.write(str(vecs[i][j]))
            if not j == len(vecs[0])-1:
                f.write("\t")
            else:
                f.write("\n")

def eigen():
    """
        Compute the eigen value and eigen vector
    """
    global vecs, vals, _arr
    vals, vecs = la.eig(_arr)


if __name__ == "__main__":
    read()
    eigen()
    write()