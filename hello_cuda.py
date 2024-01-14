from mpi4py import MPI
import cupy as cp

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# CUDA initialization
cp.cuda.Device(rank).use()

# Your CUDA-aware Python code goes here

print(f"Rank {rank}: Hello from process {rank} of {size}")