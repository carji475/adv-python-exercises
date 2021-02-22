import numpy as np

#a. Given a list of XYZ-coordinates, p, ...
print('======= Exercise a =======')
p = [[1.0, 2.0, 10],
 [3.0, 4.0, 20],
 [5.0, 6.0, 30],
 [7.0, 8.0, 40]]
pnp = np.array(p)
print(pnp/pnp[:,[-1]])

# b. Create a 3x3 ndarray. Use fancy indexing to slice out the diagonal elements.
print('\n======= Exercise b =======')
B = np.random.rand(3,3)
Bdiag =  B[[0,1,2],[0,1,2]]
print(B,Bdiag)

#c. Generate a 10 x 3 array of random numbers (all between 0 and 1). From each row, pick the number closest to 0.75. Make use of np.abs and np.argmax to find the column j which contains the closest element in each row.
print('\n======= Exercise c =======')
C = np.random.rand(10,3)
print(C,C[np.argmin(np.abs(C-0.75),0),[0,1,2]])

# d. Predict and verify the shape of the following slicing operation.
print('\n======= Exercise d =======')
x = np.empty((10, 8, 6))
idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)
print(x[idx0, idx1, idx2].shape)

# e. e. Very Advanced ...
print('\n======= Exercise e =======')
from numpy.lib.stride_tricks import as_strided
x = np.arange(12, dtype=np.int32).reshape((3, 4))
z = as_strided(x, shape=(2, 3, 2, 2),strides=(16,4,16,4))
print(z)
