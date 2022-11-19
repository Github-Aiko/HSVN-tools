import socket
import sys

# no error handling is done here, excuse me for that
hostname = sys.argv[1]

# IP lookup from hostname
print(f'The {hostname} IP Address is {socket.gethostbyname(hostname)}')