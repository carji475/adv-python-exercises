from math import exp
import numpy as np

# Cython implementation of a Radial Basis Function (RBF) approximation scheme
def rbf_network_cython(double[:,:] X, double[:] beta, double theta):
    cdef Py_ssize_t i, j, d
    cdef double r
    
    cdef Py_ssize_t N = X.shape[0]
    cdef Py_ssize_t D = X.shape[1]  
    
    Y = np.zeros(N, dtype=np.double)
    cdef double[:] Y_view = Y
        
    #N = X.shape[0]
    #D = X.shape[1]
    #Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y_view[i] = Y_view[i] + beta[j] * exp(-(r * theta)**2)

    return Y
