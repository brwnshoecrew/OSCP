import sys

userlist_file = sys.argv[1]
passlist_file = sys.argv[2]

userlist = open(userlist_file, 'r').readlines()
userlist = map(lambda s: s.strip(),userlist)
passlist = open(passlist_file, 'r').readlines()
file=open("User_Pass.txt","w+")

for username in userlist:
    count = 0
    file.write(username+":"+username+"\n")
    file.write(username+":"+username[::-1]+"\n")
    while count < 6:
        additional_normal_password = username+str(count)
        file.write(username+":"+additional_normal_password+"\n")
        additional_reversed_password = username[::-1]+str(count)
        file.write(username+":"+additional_reversed_password+"\n")
        count+=1
    for password in passlist:
        file.write(username+":"+password)
