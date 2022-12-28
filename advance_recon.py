# Import necessary modules
import subprocess
import argparse

# Set up command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("target", help="target IP address or domain")
args = parser.parse_args()

# Define the target for the scan
target = args.target

# Perform an nmap scan and save the output to a file
nmap_output = subprocess.run(["nmap", "-sV", "-oN", "nmap.txt", target], capture_output=True).stdout.decode()

# Perform a dnsenum scan and save the output to a file
dnsenum_output = subprocess.run(["dnsenum", "--enum", "--output", "dnsenum.txt", target], capture_output=True).stdout.decode()

# Perform a masscan scan and save the output to a file
masscan_output = subprocess.run(["masscan", "-p1-65535", "--output-format", "list", "--output-filename", "masscan.txt", target], capture_output=True).stdout.decode()

# Print the outputs
print(nmap_output)
print(dnsenum_output)
print(masscan_output)
