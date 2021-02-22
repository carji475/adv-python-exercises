# Program to multiply two matrices using numpy
import numpy as np

@profile
def matmult(N):
    # NxN matrix
    X = np.random.randint(0,100,(N,N))

    # Nx(N+1) matrix
    Y = np.random.randint(0,100,(N,N+1))

    # result is Nx(N+1)
    result = X@Y

    #for r in result:
    #    print(r)
    
    
N=250
matmult(N)
