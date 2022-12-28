# recon.py
A tool written in python to automate recon process

## Dependencies
```bash
# install python3, pip  and pynput


sudo apt install python3-pip

python3 -m pip install pynput

```
## Run the script with ip 
```bash

recon.py {ip}
```

# DNS recon.py


The script will prompt the user for a domain, and then perform a DNS lookup, reverse DNS lookup, and traceroute on the domain. The results will be printed to the console.

To execute this script, you can run it from the command line using the python command followed by the script name:
```bash
python recon.py
```

# recon_script.py

This script will perform a DNS lookup to get the IP address of the target domain, a reverse DNS lookup to get the hostname, a traceroute to get the hop count and IP addresses of intermediate routers, a port scan to get a list of open ports, and banner grabbing on the open ports. The results are saved to a JSON file called recon_results.json. You can modify the script to perform other recon tasks, such as HTTP header analysis or vulnerability scanning, as needed. To run the script, save it to a file and then execute it using Python 3:

```bash
python3 recon_script.py
```
### Set your url here 
![image](https://user-images.githubusercontent.com/58091942/209876529-c2f00498-2c89-4364-b3b5-d0eb9b07a8a2.png)

# advance_recon.py
Automate the process of performing a scan using tools like nmap, dnsenum, and masscan, you can create a Python script that utilizes the subprocess module to execute these tools and capture the output.
```bash
python scan.py example.com
```
This script will perform an nmap scan, a dnsenum scan, and a masscan scan on the target and save the output to separate .txt files. You can modify the script to perform additional scans or customize the arguments passed to the scanning tools as needed.
