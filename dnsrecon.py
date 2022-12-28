import subprocess

def dns_lookup(domain):
    """Perform a DNS lookup to get the IP address of a domain."""
    result = subprocess.run(["host", domain], capture_output=True).stdout.decode().split()[-1]
    return result

def reverse_dns_lookup(ip_address):
    """Perform a reverse DNS lookup to get the hostname of an IP address."""
    result = subprocess.run(["host", ip_address], capture_output=True).stdout.decode().split()[-1]
    return result

def traceroute(domain):
    """Perform a traceroute to get the hop count and IP addresses of intermediate routers."""
    result = subprocess.run(["traceroute", domain], capture_output=True).stdout.decode()
    return result

def main():
    # Get target domain from user
    domain = input("Enter a domain to perform recon on: ")
    
    # Perform recon tasks
    ip_address = dns_lookup(domain)
    hostname = reverse_dns_lookup(ip_address)
    traceroute_result = traceroute(domain)
    
    # Print results
    print(f"Domain: {domain}")
    print(f"IP address: {ip_address}")
    print(f"Hostname: {hostname}")
    print(f"Traceroute:\n{traceroute_result}")

main()
