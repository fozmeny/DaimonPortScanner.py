#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket

def daimon_scanner():
    open_ports = []
    ip_address = input("Enter the IP address to scan: ")
    port_range = input("Enter the port range to scan (separated by commas): ").split(',')
    port_range = list(map(int, port_range))
    hostname = socket.gethostbyaddr(ip_address)[0]
    print("Hostname:", hostname)
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            service = socket.getservbyport(port)
            open_ports.append((port, service))
        sock.close()
    return open_ports

open_ports = daimon_scanner()
print("Open ports: ", open_ports)


# In[ ]:




