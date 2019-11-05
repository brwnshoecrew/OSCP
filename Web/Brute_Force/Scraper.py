#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

#Using SoupStrainer is faster than not if you have a specific tag, string, etc. you're looking for.
#You define the filter applied via SoupStrainer to a variable that is passed as an argument to BeautfiulSoup.
#Without SoupStrainer, BeautifulSoup would re-evaluate the entire HTML page content for each command.
a_links = SoupStrainer("a")

#Capture the response of a GET request in the response variable.
response = requests.get("https://www.crummy.com/software/BeautifulSoup")
#Assign the content of the response to the transfer_variable for usage in BeautifulSoup
transfer_variable = response.content

#We assign the values of each instance within the response.content(transfer_variable) that match the filter defined in the SoupStrainer variable using the html.parser parser.
for result in BeautifulSoup(transfer_variable, 'html.parser', parse_only=a_links):
    #We assign the value of the href key (key:value pair) tothe string variable
    string = result.get('href')
    #If string is a NoneType value (meaning that there wasn't any value assigned for that instance of the href key), then we reassign the value from NoneType to 'This is None' so it bypasses the next filter to only display lines starting with 'http' characters.
    if string is None:
        string = "This is None"
    #If the string starts with the 'http' characters, then it is a web address which is what we want to isolate and display to the screen.
    if string.startswith('http'):
        print(string)
