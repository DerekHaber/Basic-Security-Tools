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