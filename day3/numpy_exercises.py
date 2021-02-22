import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
print('======= Exercise a =======')
a = np.zeros(10)
a[4] = 1
print(a)

# b. Create a vector with values ranging from 10 to 49
print('\n======= Exercise b =======')
b = np.arange(10,50)
print(b)

# c. Reverse a vector (first element becomes last)
print('\n======= Exercise c =======')
c = np.random.rand(5)
print(c)
crev = c[::-1]
print(crev)

# d. Create a 3x3 matrix with values ranging from 0 to 8
print('\n======= Exercise d =======')
A = np.arange(0,9).reshape((3,3))
print(a)

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
print('\n======= Exercise e =======')
e = np.array([1,2,0,0,4,0])
nonzero_indices = np.where(e!=0)[0]
print(nonzero_indices)

# f. Create a random vector of size 30 and find the mean value
print('\n======= Exercise f =======')
print(np.random.rand(30).mean())

# g. Create a 2d array with 1 on the border and 0 inside
print('\n======= Exercise g =======')
n = 5
G = np.zeros((n,n))
G[0,:] = 1
G[-1,:] = 1
G[:,0] = 1
G[:,-1] = 1
print(G)

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
print('\n======= Exercise h =======')
n = 8
H = np.zeros((n,n))
H[0::2,0::2] = 1
H[1::2,1::2] = 1
print(H)

# i. Create a checkerboard 8x8 matrix using the tile function
print('\n======= Exercise i =======')
I = np.zeros(2*n)
I[0:n:2]=1
I[n+1::2]=1
I = np.tile(I.reshape((2,n)),(round(n/2),1))
print(I)

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
print('\n======= Exercise j =======')
Z = np.arange(11)
Z[(Z>2) & (Z<9)] *= -1
print(Z)

# k. Create a random vector of size 10 and sort it
print('\n======= Exercise k =======')
Z = np.random.random(10)
Z.sort()
print(Z)

# l. Consider two random array A anb B, check if they are equal
print('\n======= Exercise l =======')
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print(equal)

# m. How to convert an integer (32 bits) array into a float (32 bits) in place?
print('\n======= Exercise m =======')
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z.dtype = np.float32
print(Z.dtype)

# n. How to get the diagonal of a dot product?
print('\n======= Exercise n =======')
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(D)


















