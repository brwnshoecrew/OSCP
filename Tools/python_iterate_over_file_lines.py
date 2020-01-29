#!/usr/bin/python3

#Open a file.  You can just as easily convert this into a user-input field that is used as input.
file = open('C:\\Users\\vorhem1\\Desktop\\list.txt', 'r')

#With syntax to read large files.  It transfers the entire contents of a file into memory for opreations within the block.
#File object is automatically closed after existing the with block and automatically handles exceptions within the block.
with file as f:
    #Define IP_Address variable as a list.
    IP_Address = []
    #The 'line' variable is automatically created for each line in a txt file which we can use to perform operations over multiple lines.
    for line in f:
        #Whatever operations we want to do over each line of the file.

        #Strip the \n character from each line of the text file so it doesn't get stored in the list variable.
        #Split the one line entry into two seperate entries by the delimeter character /
        line = line.rstrip().split('/')
        #Append the tuple of site name and IP address to the IP_Address list variable.
        IP_Address.append(line[0])
    #Working from inside to out.
    #list(dict.fromkeys(XX)) - This deletes duplicate entries in the XX list variable.
    #sorted - Sorts the resulting non-duplicate XX list variable.
    #"\n".join - Prints each of the resulting sorted, non-duplicate XX list variable entries on a new line.
    print("\n".join(sorted(list(dict.fromkeys(IP_Address)))))
