import os

from pynput.keyboard import Key, Controller

keyboard = Controller()
ip = input("Please enter a target: ")

os.system(f"nmap -A -p 80 {ip} -v >> nmap.txt")
os.system(f"smbclient -N -L {ip} >> smbclient.txt")
os.system(f"smbmap -H {ip} >> smbmap.txt")

keyboard.press(Key.enter)
keyboard.release(Key.enter)
