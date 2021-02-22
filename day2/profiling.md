# 3a)
## speed
Profiled using 

`kernprof -l -v matmult.py`

From the printout below, it is clear that the bottleneck is the nested for-loop in which the result is computed. 
For-loops in general are (very) slow in python, so this is where we need to optimise!


```
Wrote profile results to matmult.py.lprof
Timer unit: 1e-06 s

Total time: 24.2299 s
File: matmult.py
Function: matmult at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def matmult(N):
     6                                               # NxN matrix
     7         1          1.0      1.0      0.0      X = []
     8       251        263.0      1.0      0.0      for i in range(N):
     9       250     287845.0   1151.4      1.2          X.append([random.randint(0,100) for r in range(N)])
    10                                           
    11                                               # Nx(N+1) matrix
    12         1          1.0      1.0      0.0      Y = []
    13       251        221.0      0.9      0.0      for i in range(N):
    14       250     284193.0   1136.8      1.2          Y.append([random.randint(0,100) for r in range(N+1)])
    15                                           
    16                                               # result is Nx(N+1)
    17         1          1.0      1.0      0.0      result = []
    18       251        132.0      0.5      0.0      for i in range(N):
    19       250        468.0      1.9      0.0          result.append([0] * (N+1))
    20                                           
    21                                               # iterate through rows of X
    22       251        251.0      1.0      0.0      for i in range(len(X)):
    23                                                   # iterate through columns of Y
    24     63000      37143.0      0.6      0.2          for j in range(len(Y[0])):
    25                                                       # iterate through rows of Y
    26  15750250    9265519.0      0.6     38.2              for k in range(len(Y)):
    27  15687500   14353842.0      0.9     59.2                  result[i][j] += X[i][k] * Y[k][j]
```

## memory
Profiled using 

`python -m memory_profiler matmult.py` 

Roughtly the same amount of memory (~ 0.5 MiB) is being used when building each of X and Y, and when allocating the result (lines 9, 14 and 19). The singlest biggest cost is created by the range command on line 26, which surely is a consequence of the high number of occurences.

```
Filename: matmult.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4   39.297 MiB   39.297 MiB           1   @profile
     5                                         def matmult(N):
     6                                             # NxN matrix
     7   39.297 MiB    0.000 MiB           1       X = []
     8   39.723 MiB    0.000 MiB         251       for i in range(N):
     9   39.723 MiB    0.426 MiB       63250           X.append([random.randint(0,100) for r in range(N)])
    10                                         
    11                                             # Nx(N+1) matrix
    12   39.723 MiB    0.000 MiB           1       Y = []
    13   40.238 MiB    0.000 MiB         251       for i in range(N):
    14   40.238 MiB    0.516 MiB       63500           Y.append([random.randint(0,100) for r in range(N+1)])
    15                                         
    16                                             # result is Nx(N+1)
    17   40.238 MiB    0.000 MiB           1       result = []
    18   40.754 MiB    0.000 MiB         251       for i in range(N):
    19   40.754 MiB    0.516 MiB         250           result.append([0] * (N+1))
    20                                         
    21                                             # iterate through rows of X
    22   42.688 MiB    0.000 MiB         251       for i in range(len(X)):
    23                                                 # iterate through columns of Y
    24   42.688 MiB    0.000 MiB       63000           for j in range(len(Y[0])):
    25                                                     # iterate through rows of Y
    26   42.688 MiB    1.934 MiB    15750250               for k in range(len(Y)):
    27   42.688 MiB    0.000 MiB    15687500                   result[i][j] += X[i][k] * Y[k][j]
```

# 3b
## speed
Profiled using 

`kernprof -l -v euler72.py`

We find that most time is being spent in the factorize-function. The call to factorize dominates the time consumed by the fast-phi-function, corresponding to roughly half the total time. Inside the factorize function, most time is spent on the while-loop.

```
30397485.0
Wrote profile results to euler72.py.lprof
Timer unit: 1e-06 s

Total time: 0.005856 s
File: euler72.py
Function: gen_primes at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def gen_primes(n):
     6         1          2.0      2.0      0.0      l = range(2,n)
     7         1          1.0      1.0      0.0      primes = []
     8       999        356.0      0.4      6.1      for j in range(0,len(l)):
     9       998        341.0      0.3      5.8          p = True
    10      2968       1021.0      0.3     17.4          for d in primes:
    11      2967       1678.0      0.6     28.7              if(d > sqrt(l[j])):
    12       167         62.0      0.4      1.1                  break
    13      2800       1396.0      0.5     23.8              if(l[j] % d == 0):
    14       830        308.0      0.4      5.3                  p = False
    15       830        289.0      0.3      4.9                  break;
    16       998        322.0      0.3      5.5          if(p):
    17       168         80.0      0.5      1.4              primes.append(l[j])
    18                                           
    19         1          0.0      0.0      0.0      return primes

Total time: 0.158893 s
File: euler72.py
Function: factorize at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def factorize(n,primes):
    23      9999       3352.0      0.3      2.1      factors = []
    24      9999       3079.0      0.3      1.9      init_n = n
    25     96347      29893.0      0.3     18.8      for p in primes:
    26    118736      51902.0      0.4     32.7          while(n%p == 0):
    27     22389       7963.0      0.4      5.0              n = n/p
    28     22389       9108.0      0.4      5.7              factors.append(p)
    29     96347      39722.0      0.4     25.0          if(p > sqrt(n)):
    30      9999       3233.0      0.3      2.0              break
    31      9999       3703.0      0.4      2.3      if(n > 1):
    32      9596       3876.0      0.4      2.4          factors.append(n)
    33      9999       3062.0      0.3      1.9      return factors

Total time: 0.336101 s
File: euler72.py
Function: fast_phi at line 50

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    50                                           @profile
    51                                           def fast_phi(n,primes):
    52      9999     294070.0     29.4     87.5      factors = factorize(n,primes)
    53      9999       3904.0      0.4      1.2      phi = factors[0]-1
    54     31985      14324.0      0.4      4.3      for i in range(1,len(factors)):
    55     21986      10010.0      0.5      3.0          if(factors[i] == factors[i-1]):
    56      7685       4438.0      0.6      1.3              phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    57                                                   else:
    58     14301       6311.0      0.4      1.9              phi *= (factors[i]-1)
    59      9999       3044.0      0.3      0.9      return phi
```


## memory
Profiled using 

`python -m memory_profiler euler72.py`
 
It seems that the memory is exclusively consumed by the factorize-function called on line 52.
 
``` 
30397485.0
Filename: euler72.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4   39.535 MiB   39.535 MiB           1   @profile
     5                                         def gen_primes(n):
     6   39.535 MiB    0.000 MiB           1       l = range(2,n)
     7   39.535 MiB    0.000 MiB           1       primes = []
     8   39.535 MiB    0.000 MiB         999       for j in range(0,len(l)):
     9   39.535 MiB    0.000 MiB         998           p = True
    10   39.535 MiB    0.000 MiB        2968           for d in primes:
    11   39.535 MiB    0.000 MiB        2967               if(d > sqrt(l[j])):
    12   39.535 MiB    0.000 MiB         167                   break
    13   39.535 MiB    0.000 MiB        2800               if(l[j] % d == 0):
    14   39.535 MiB    0.000 MiB         830                   p = False
    15   39.535 MiB    0.000 MiB         830                   break;
    16   39.535 MiB    0.000 MiB         998           if(p):
    17   39.535 MiB    0.000 MiB         168               primes.append(l[j])
    18                                         
    19   39.535 MiB    0.000 MiB           1       return primes


Filename: euler72.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21   39.535 MiB 395312.027 MiB        9999   @profile
    22                                         def factorize(n,primes):
    23   39.535 MiB    0.000 MiB        9999       factors = []
    24   39.535 MiB    0.000 MiB        9999       init_n = n
    25   39.535 MiB    0.000 MiB       96347       for p in primes:
    26   39.535 MiB    0.000 MiB      118736           while(n%p == 0):
    27   39.535 MiB    0.000 MiB       22389               n = n/p
    28   39.535 MiB    0.000 MiB       22389               factors.append(p)
    29   39.535 MiB    0.000 MiB       96347           if(p > sqrt(n)):
    30   39.535 MiB    0.000 MiB        9999               break
    31   39.535 MiB    0.000 MiB        9999       if(n > 1):
    32   39.535 MiB    0.000 MiB        9596           factors.append(n)
    33   39.535 MiB    0.000 MiB        9999       return factors


Filename: euler72.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    50   39.535 MiB   39.535 MiB        9999   @profile
    51                                         def fast_phi(n,primes):
    52   39.535 MiB 395312.027 MiB        9999       factors = factorize(n,primes)
    53   39.535 MiB    0.000 MiB        9999       phi = factors[0]-1
    54   39.535 MiB    0.000 MiB       31985       for i in range(1,len(factors)):
    55   39.535 MiB    0.000 MiB       21986           if(factors[i] == factors[i-1]):
    56   39.535 MiB    0.000 MiB        7685               phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    57                                                 else:
    58   39.535 MiB    0.000 MiB       14301               phi *= (factors[i]-1)
    59   39.535 MiB    0.000 MiB        9999       return phi
``` 

# 3c
Used numpy instead, reduced the time to 0.021084 s.
See `matmult_improved.py`
