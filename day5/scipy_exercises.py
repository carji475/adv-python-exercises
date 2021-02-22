from scipy import linalg as sla
from scipy import stats as st
import numpy as np
from matplotlib import pyplot as plt

## Linear algebra
# a
A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

# b
b = np.array([1,2,3])

# c
x = sla.solve(A, b)

# d
print('\nAx-b\n', A@x-b)

# e
B = np.random.rand(3,3)
X = sla.solve(A, B)
print('\nA*X-B\n', A@X-B) # inaccurate due to illconditioning

# f
lam, V = sla.eig(A)
print('\nlam\n', lam,'\nV\n', V, '\nAV-lam*V\n', A@V-lam*V)

# g
invA = sla.solve(A, np.eye(A.shape[0]))
detA = sla.det(A) 
print('\nA*invA\n', A@invA, '\ndet A\n', detA)

# h
norm1 = sla.norm(A, ord=1)
norm2 = sla.norm(A, ord=2)
normInf = sla.norm(A, ord=np.inf)
normFro = sla.norm(A, ord='fro')
print('\nnorm1 of A\n', norm1, '\nnorm2 of A\n', norm2, \
    '\nnormInf of A\n', normInf,'\nnormFro of A\n', normFro,)


## Statistics
# a
fig, ax = plt.subplots(1, 3)
x = np.arange(20)
mu = 5
popmf = st.poisson.pmf(x, mu)
ax[0].stem(x,popmf)
ax[0].set_title('pmf')
pocdf = st.poisson.cdf(x, mu)
ax[1].stem(x,pocdf)
ax[1].set_title('cdf')
n=1000
posamples = st.poisson.rvs(mu, size=n)
ax[2].hist(posamples, x, align='left', density=True, rwidth=0.5)
ax[2].set_title('Density histogram of '+str(n)+' samples')
plt.show()

# b
fig, ax = plt.subplots(1, 3)
x = np.linspace(-3,3,100)
mu = 0
sig = 1
normpdf = st.norm.pdf(x, mu, sig)
ax[0].plot(x,normpdf)
ax[0].set_title('pdf')
normcdf = st.norm.cdf(x, mu, sig)
ax[1].plot(x,normcdf)
ax[1].set_title('cdf')
n=1000
normsamples = st.norm.rvs(mu, sig, size=n)
ax[2].hist(normsamples,density=True, rwidth=1.0)
ax[2].set_title('Density histogram of '+str(n)+' samples')
plt.show()

# c
print('\nBoth poisson\n',st.ttest_ind(st.poisson.rvs(mu, size=n),st.poisson.rvs(mu, size=n)))
print('\nPoisson & normal\n',st.ttest_ind(st.norm.rvs(mu, sig, size=n),st.poisson.rvs(mu, size=n)))
print('\nBoth normal\n',st.ttest_ind(st.norm.rvs(mu, sig, size=n),st.norm.rvs(mu, sig, size=n)))








