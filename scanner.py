#Python Port Scanner

import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner1 = pyfiglet.figlet_format("S I M P L E")
ascii_banner2 = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner1)
print(ascii_banner2)

if len(sys.argv) == 2:

	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount for argument: You must enter the IP address!")

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("_" * 50)

try:

	for port in range(1,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
	
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\n Exiting Program Now!")
	sys.exit()
except socket.gaierror:
	print("\n Hostname could not be resolved!")
	

