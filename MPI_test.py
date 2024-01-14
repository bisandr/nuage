import os
import subprocess

# Run the command to check MPI version
result = subprocess.run(['mpiexec', '--version'], stdout=subprocess.PIPE)

# Print the result
print(result.stdout.decode())