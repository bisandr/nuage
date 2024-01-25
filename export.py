import torch
import os
import subprocess

# Get the current date, commit sequence, and image information using subprocess
day = subprocess.check_output(["date", "+%Y%m%d"]).decode().strip()
commit_seq = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
image = "arbre"

# Set the log directory using f-string
logdir = f'OUTPUT/sinddpm-{image}-{day}-{commit_seq}'

# Set the environment variable LOGDIR
os.environ['LOGDIR'] = logdir

# Create the directory if it doesn't exist
os.makedirs(logdir, exist_ok=True)

# Create a tensor using PyTorch
x = torch.rand(5, 3)

# Print the tensor
print(x)

# Save the output to a log file in the specified directory
log_file_path = os.path.join(logdir, 'output_log.txt')
with open(log_file_path, 'w') as log_file:
    log_file.write(str(x))

# Print a message indicating where the log file is saved
print(f"Output saved to: {log_file_path}")
