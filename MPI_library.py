try:
    from mpi4py import MPI
    print("MPI library is available.")
except ImportError:
    print("MPI library is not available.")
