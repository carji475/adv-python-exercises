import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

myrank = np.zeros(1)
rank_sum = np.zeros(1)

myrank[0] = rank

comm.Reduce(myrank, rank_sum, op=MPI.SUM, root=0)

if rank==0:
    print("Sum of ranks: ", rank_sum.item())


