# Import required modules
import subprocess
import json

# Target domain
domain = "example.com"

# Perform DNS lookup to get IP address
ip_address = subprocess.run(["host", domain], capture_output=True).stdout.decode().split()[-1]

# Perform reverse DNS lookup to get hostname
hostname = subprocess.run(["host", ip_address], capture_output=True).stdout.decode().split()[-1]

# Perform traceroute to get hop count and IP addresses of intermediate routers
traceroute = subprocess.run(["traceroute", domain], capture_output=True).stdout.decode()

# Perform port scan to get open ports
port_scan = subprocess.run(["nmap", "-sT", domain], capture_output=True).stdout.decode()

# Extract open ports from port scan output
open_ports = []
for line in port_scan.splitlines():
  if "open" in line:
    open_ports.append(line.split("/")[0])

# Perform banner grabbing on open ports
banners = {}
for port in open_ports:
  banner = subprocess.run(["nc", "-v", domain, port], capture_output=True).stdout.decode()
  banners[port] = banner

# Save results to JSON file
results = {
  "domain": domain,
  "ip_address": ip_address,
  "hostname": hostname,
  "traceroute": traceroute,
  "port_scan": port_scan,
  "banners": banners
}

with open("recon_results.json", "w") as f:
  json.dump(results, f)
