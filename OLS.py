# Lib
import numpy as np
from numpy.linalg import inv #inverse matrix

def OLS(X,y):
    Beta = inv((X.T.dot(X))).dot(X.T.dot(y))
    
    return Beta