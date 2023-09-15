#!/usr/bin/python3
import nmap

scanner = nmap.PortScanner()

print('Custom NMAP Automation Tool')
print('____________________________________')

ip_addr = input('Enter IP here: ')
print('The IP you entered is: ', ip_addr)
type(ip_addr)


resp = input("""\nScan type:
             1) Syn Ack
             2) UDP
             3) Comprehensive""")
print('Starting ', resp)

# Setting up Syn Ack scan
if resp == "1":
    print('Nmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS') # Starts Syn Ack scan on ports 1-1024
    print(scanner.scaninfo()) # Prints scan info
    print('IP Up? ', scanner[ip_addr].state()) # States whether provided IP Address is running
    print(scanner[ip_addr].all_protocols()) # Port type? TCP or UDP
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
