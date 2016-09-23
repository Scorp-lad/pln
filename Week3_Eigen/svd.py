import numpy as np
import random

needZero = lambda x: False if x < 0.5 else True
step = lambda x: 1 if x > 0.5 else 0

def randomZero(arr):
    h, w = np.shape(arr)
    for i in range(h):
        for j in range(w):
            if needZero(random.randint(0, 1)*2):
                arr[i][j] = 0
            """
            else:  
                arr[i][j] = 1
            """
    return arr

def Thresh(arr):
    h, w = np.shape(arr)
    for i in range(h):
        for j in range(w):
            arr[i][j] = step(arr[i][j])
    return arr

def SVD(img, discard=0, reduction=False):
    """
        Do singular value decomposition and return the matrix

        Arg:    image and the discard index
        Ret:    A hat, U, S and V
                A hat   - Result matrix
                U       - Left singular matrix
                S       - Singular value diagonal matrix
                V       - Right singular matrix
    """
    # Check the validity of the parameter
    h, w = np.shape(img)
    if discard > max(h, w):
        print "Invalid discard index..."
        return None
    imgSvd = np.zeros((h, w))

    # Do svd
    if discard == 0:
        imgU, imgS, imgV = np.linalg.svd(img, full_matrices=False)
        #imgS_ = imgS
        imgS_ = np.diag(imgS)
        print imgU.shape, imgS_.shape, imgV.shape
        np.allclose(imgSvd, np.dot(imgU, np.dot(imgS_, imgV)))
        return np.dot(imgU, np.dot(imgS_, imgV)), imgU, imgS_, imgV 
    elif reduction == True:
        imgU, imgS, imgV = np.linalg.svd(img, full_matrices=False)
        imgU_, imgS_, imgV_ = imgU, imgS, imgV
        imgS_[min(h, w)-discard:] = 0
        imgS_ = np.diag(imgS)
        imgU_ = imgU * imgS_
        imgV_ = np.matmul(imgS_, imgV)
        np.allclose(imgSvd, np.dot(imgU_, np.dot(imgS_, imgV_)))
        return np.dot(imgU_, np.dot(imgS_, imgV_)), imgU_, imgS_, imgV_
    else:
        imgU, imgS, imgV = np.linalg.svd(img, full_matrices=False)
        imgS_ = imgS
        imgS_[min(h, w)-discard:] = 0
        imgS_ = np.diag(imgS)
        np.allclose(imgSvd, np.dot(imgU, np.dot(imgS_, imgV)))
        return np.dot(imgU, np.dot(imgS_, imgV)), imgU, imgS_, imgV

def test():
    """
        Testing function
    """
    img = np.random.rand(2, 3)
    img = randomZero(img)
    img = np.asarray([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    """
    imgSvd = np.zeros((300, 500))
    imgU, imgS, imgV = np.linalg.svd(img, full_matrices=False)


    # Discard 100 character
    imgU_, imgS_, imgV_ = imgU, imgS, imgV
    #imgS_[250:] = 0
    imgS_ = np.diag(imgS)
    #imgU_ = imgU * imgS_
    #imgV_ = np.matmul(imgS_, imgV)

    print imgU_.shape, imgS_.shape, imgV_.shape
    np.allclose(imgSvd, np.dot(imgU_, np.dot(imgS_, imgV_)))
    imgSvd = np.dot(imgU_, np.dot(imgS_, imgV_))
    #imgSvd = Thresh(imgSvd)
    """
    imgSvd, u, s, v = SVD(img, discard=2, reduction=False)

    # Show
    #print "singular shape: ", imgS.shape
    print "origin: ", img
    print ""
    print "reduce: ", imgSvd
    print ""
    print "difference: ", img-imgSvd

#test()