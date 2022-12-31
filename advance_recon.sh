#!/bin/bash

# Prompt the user for the target domain or IP address
echo "Enter the target domain or IP address:"
read target

# Create a new folder with the target's name
mkdir $target

# Set the output file
output_file=$target/$target.txt

# Perform a DNS lookup to get the IP address for the target
ip_address=$(dig +short $target)

# Perform a reverse DNS lookup to get the hostname for the target
hostname=$(dig -x $ip_address +short)

# Perform a whois lookup to get the registration information for the target
whois=$(whois $target)

# Perform a traceroute to get the route taken by packets to the target
traceroute=$(traceroute $target)

# Perform a nmap scan to get information about the open ports on the target
nmap=$(nmap $target)

# Use the dmitry tool to gather additional information about the target
dmitry=$(dmitry -winseo $target)

# Use the fierce tool to perform DNS reconnaissance on the target
fierce=$(fierce -dns $target)

# Use the theharvester tool to gather email addresses and subdomains related to the target
theharvester=$(theharvester -d $target -b all)

# Use the whatweb tool to identify the technologies used by the target
whatweb=$(whatweb $target)

# Output the results of the reconnaissance to the terminal and the output file
echo "IP address: $ip_address"
echo "Hostname: $hostname"
echo "Whois information: $whois"
echo "Traceroute: $traceroute"
echo "Nmap scan: $nmap"
echo "Dmitry results: $dmitry"
echo "Fierce results: $fierce"
echo "TheHarvester results: $theharvester"
echo "WhatWeb results: $whatweb"
echo ""
echo "Advanced reconnaissance complete. Results saved to $output_file."
echo ""
echo "IP address: $ip_address" > $output_file
echo "Hostname: $hostname" >> $output_file
echo "Whois information: $whois" >> $output_file
echo "Traceroute: $traceroute" >> $output_file
echo "Nmap scan: $nmap" >> $output_file
echo "Dmitry results: $dmitry" >> $output_file
echo "Fierce results: $fierce" >> $output_file
echo "TheHarvester results: $theharvester" >> $output_file
echo "WhatWeb results: $whatweb" >> $output_file
