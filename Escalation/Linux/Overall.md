# General Recommendations
- Basic system info (OS/Kernel/System name, etc) 
- Networking Info (ifconfig, route, netstat, etc) 
- Miscellaneous filesystem info (mount, fstab, cron jobs, etc) 
- User info (current user, all users, super users, command history, etc) 
- File and Directory permissions (world-writeable files/dirs, suid files, root home directory) 
- Files containing plaintext passwords  
- Interesting files, processes and applications (all processes and packages, all processes run by root and the associated packages, sudo version, apache config file, etc)
- All installed languages and tools (gcc, perl, python, nmap, netcat, wget, ftp, etc)

# Exam Tip
Remember, they want you use a specific technique.  Enumerate and run this:
```
which awk perl python ruby gcc cc vi vim nmap find netcat nc wget tftp ftp 2>/dev/null
```
This will give you a good idea of what language the priv esc is typically using.  If you don’t see a compiler such as GCC, you know it’s probably not going to be a kernel exploit.
