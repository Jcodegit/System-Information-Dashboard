#!/usr/bin/env python3

import platform
import socket
import psutil
import os
import datetime
import time
import shutil

print("="*40, "System Information", "="*40)

# Function to get IP address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Hostname
hostname = socket.gethostname()

# OS version
system = platform.system()
release = platform.release()

# Uptime
boot_time = psutil.boot_time()
seconds = time.time() - boot_time
seconds = int(seconds)
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

# Disk free
if os.name == "nt":
    path = "C:\\"
else:
    path = "/"

total, used, free = shutil.disk_usage(path)

# RAM Usage
mem = psutil.virtual_memory()

# CPU Usage
cpu = psutil.cpu_percent(interval=1)

# Logged In User
user = os.getlogin()

# Output
print("Hostname: ",hostname)
print(f"User: {user}")
print("IP address: ",get_ip())

print("OS Release: ",system, release)

print(f"Uptime: {hours} Hours {minutes} Minutes {seconds} Seconds")

print(f"CPU Usage: {cpu}%")

print(f"Disk Total: {total // (1024**3)} GB")
print(f"Disk Used:  {used // (1024**3)} GB")
print(f"Disk Free:  {free // (1024**3)} GB")

print(f"RAM Total: {mem.total // (1024**3)} GB") 
print(f"RAM Used: {mem.used // (1024**3)} GB")
print(f"RAM Free: {mem.available // (1024**3)} GB")
