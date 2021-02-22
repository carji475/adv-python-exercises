# Speed optimization using Cython
## b) 
The naive implementation takes about 6 s, and the Scipy version about 0.1 s (i.e. around 60 times faster).

## c) 
Profiling using `kernprof -l -v rbf.py`, see output below.
The naive implementation is spending a lot of time in the nested for loop, which are very inefficient in python. Scipy has the routine implemented in a low-level language.

## d) 
Getting some some advice from the Cython documentation (http://docs.cython.org/en/latest/src/userguide/numpy_tutorial.html), i cut the time down to around 0.2 s. 
See `fastloop.pyx`.

```
Wrote profile results to rbf.py.lprof
Timer unit: 1e-06 s

Total time: 13.3469 s
File: rbf.py
Function: rbf_network at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def rbf_network(X, beta, theta):
     8                                           
     9         1          3.0      3.0      0.0      N = X.shape[0]
    10         1          1.0      1.0      0.0      D = X.shape[1]
    11         1          7.0      7.0      0.0      Y = np.zeros(N)
    12                                           
    13      1001        449.0      0.4      0.0      for i in range(N):
    14   1001000     481359.0      0.5      3.6          for j in range(N):
    15   1000000     473506.0      0.5      3.5              r = 0
    16   6000000    2875394.0      0.5     21.5              for d in range(D):
    17   5000000    6821867.0      1.4     51.1                  r += (X[j, d] - X[i, d]) ** 2
    18   1000000     752785.0      0.8      5.6              r = r**0.5
    19   1000000    1941510.0      1.9     14.5              Y[i] += beta[j] * exp(-(r * theta)**2)
    20                                           
    21         1          0.0      0.0      0.0      return Y

Total time: 0.238659 s
File: rbf.py
Function: rbf_scipy at line 24

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    24                                           @profile
    25                                           def rbf_scipy(X, beta):
    26                                           
    27         1          3.0      3.0      0.0      N = X.shape[0]
    28         1          1.0      1.0      0.0      D = X.shape[1]    
    29         1     202020.0 202020.0     84.6      rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta)
    30                                               #Xtuple = tuple([X[:, i] for i in range(D)])
    31         1         25.0     25.0      0.0      Xtuple = tuple([X[:, i] for i in range(D)])
    32                                           
    33         1      36610.0  36610.0     15.3      return rbf(*Xtuple)
```
