# Python Port Scanner
# Name: Ruben Ramirez
#
#  Specs: Performs a TCP port scan using python's nmap
#         library. The program prompts the user to supply
#         a host name and a set of ports to scan. After 
#         the scan is performed, a report is printed which
#         shows the name of the scanner ports, along with
#         the state of the port.
#         

import nmap
import socket

def nmapScan(host, ip, port):
    """Performs a tcp port scan of a given host"""
    try:
        nmScan = nmap.PortScanner()
        nmScan.scan(ip, str(port))
        state = nmScan[ip]['tcp'][int(port)]['state']
        name = nmScan[ip]['tcp'][int(port)]['name']
        print("* tcp/" + port + " " + \
                state + " " + name)
    except:
        print("Unable to attain information for port "\
                + port)
        pass

# Prompt user for target information
host = input("Host Name: ") 
ports = input("Port[s]: ")
ports = ports.split()

if host == None or ports[0] == None:
    print("You must specify a target host and port[s].")
    exit(0)

ip = socket.gethostbyname(host)
print("Scan results for: " + host + " (" + ip + ")")
for port in ports:
    nmapScan(host, ip, port)
