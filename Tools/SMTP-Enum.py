#!/usr/bin/python 
#Import socket to open a raw socket to SMTP port 25
import socket
#Import system to capture command line arguments
import sys 
#Library used to easily capture and organize flags used by the program for arguments received via the command line.
import argparse

#Declare the parser variable and include a description of how to use the program if the user uses in the -h / --help flags.
parser = argparse.ArgumentParser(description='Usage: SMTP-Enum.py [-f/--file] User file location [--IP] IP address [-p/--port] Port.')
#Define arguments that can be used by the program.  -f/--file is the file location of the username list. --IP is the IP address the enumeration script will run over.
parser.add_argument('-f', '--file', action="store", dest="up_file_var", required=True, metavar='Username File', help='The location of the username list to be tried against the SMTP VRFY service.')
parser.add_argument('--IP', action="store", dest="IP_var", required=True, metavar='SMTP IP', help='The IP address running the SMTP service to enumerate users on.')
parser.add_argument('-uP', '--user', action="store", dest="user_param_var", metavar='Single User Paramter', help='A signle username paramter to verify against the SMTP service.')
parser.add_argument('-o', '--outfile', action="store", dest="outfile_var", metavar='Output File Location', help='The output file containing the results of the script execution.')
parser.add_argument('-p', '--port', action="store", dest="port_var", required=True, metavar='SMTP Port', help='The port the SMTP service is listening on.')
args = parser.parse_args()

#Accessing the username:password text file   
up_file = open(args.up_file_var,"r")
#Create / open the output file to hold the results of the command.
out_file = open(args.outfile_var,"w+")


#Load the username list and iterate through all line entries 
for username in up_file:
    #Create a Socket 
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  
    #Convert port variable to integer as the s.connect command next requires the port number to be an integer type
    args.port_var = int(args.port_var)

    #Connect to the Server
    connect=s.connect((args.IP_var,args.port_var))  
  
    #Receive the banner 
    banner=s.recv(1024)

    #VRFY each username
    s.send('VRFY ' + username) 
    result=s.recv(1024) 

    #Only print out the username that resulted in a successful VRFY result
    if "2.0.0" in result:
        result = result[10:].strip()
        print result
    
        #Write successful results to the outfile.
        out_file.write(result+"\n")

    #Close the SMTP connection
    s.close()

#It is good practice to close the files at the end to free up resources
up_file.close()
out_file.close()

#Print end note to CLI
print "SMTP Enumeration done.  Results written to file at",args.outfile_var
