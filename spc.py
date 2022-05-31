#Python Port Scanner

import pyfiglet   # pyfiglet takes ASCII text and renders it in ASCII art fonts.
import sys         # The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
import socket       # This module provides access to the socket interface.
from datetime import datetime   # Datetime module supplies classes to work with date and time.

ascii_banner1 = pyfiglet.figlet_format("S I M P L E")  # Define Variables with banner content
ascii_banner2 = pyfiglet.figlet_format("PORT SCANNER") # Define Variables with banner content
print(ascii_banner1)   # Print banner
print(ascii_banner2)

if len(sys.argv) == 2:       # len returns the bumber of items in a list. We're setting up a conditional for 2 items
                             # The 1st item in the system argument should be the name of the script. The second should be the IP address
	target = socket.gethostbyname(sys.argv[1])   # Here we're defining the variable 'target' as the function gethostname from the socket module with the IP address given as the argument
else:                                         # If there wasn't an IP address, we'll let the user know we need one
	print("Error! You must enter the IP after the script name when executing")

print("_" * 50)   # This is just aeshetics printing a line
print("Scanning Target: " + target)   # let the user know we are now scanning the IP he supplied
print("Scanning started at:" + str(datetime.now())) # let the user know when we started
print("_" * 50)   # print another line

try:                                               # use a try except statement to properly deal with errors while scanning

	for port in range(1,65535):                               # Create For loop that using of range of 1-265535 for all an IP's ports
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Here we made a socket instance and passed it two parameters. The first parameter is AF_INET which refers to the address-family ipv4. The second one is SOCK_STREAM a connection-oriented TCP protocol.
		socket.setdefaulttimeout(1)                             # Here we set a timeout so we're not left hanging if there's a failure to connect
	
		result = s.connect_ex((target,port))           # s.connect_ex attempt to connect to the target/IP and port abd returns an error code
		if result ==0:                                 # An error code of 0 means a successful connection
			print("Port {} is open".format(port))        # Let the user know a connection was successful
		s.close()                                      # close the socket/'s'
		
except KeyboardInterrupt:                 # If there's a keyboard interruption, quit and let the user know
	print("\n Exiting Program Now!")
	sys.exit()
except socket.gaierror:                   # If there's a problem with the IP address, let the user know
	print("\n Hostname could not be resolved!")
