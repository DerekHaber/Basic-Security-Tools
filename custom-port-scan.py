import pyfiglet
import sys
import socket
from datetime import datetime
  
ascii_banner = pyfiglet.figlet_format("CUSTOM PORT SCAN")
print(ascii_banner)
print('by Derek Haber')

# Defining a target
target = input('Target IP: ')
 

# defining port range
port_range = 1,65535


# Add Banner
print("-" * 50)
print("Target: " + target)
print("Started at: " + str(datetime.now()))
print("-" * 50)
  

def get_open_ports():
            # will scan ports between 1 to 65,535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("{} ".format(port), )
        s.close()
try:
     get_open_ports()

         
except KeyboardInterrupt:
        print("\n Scan Cancelled")
        sys.exit()
except socket.gaierror:
        print("\n HUnresolved Hostname")
        sys.exit()
except socket.error:
        print("\ not responding")
        sys.exit()
