# Python library to wrap and consume the most used URL shorteners APIs.
pip install pyshorteners


#importing the required module
import pyshorteners


#change for every URL shortener’s APIs
long_url = input("Enter the URL to shorten: ")

#library’s class object to start shortening our URLs
type_tiny = pyshorteners.Shortener() 

#name along with the location of the PDF
short_url = type_tiny.tinyurl.short(long_url)
print("The Shortened URL is: " + short_url )


#Other example Shorten URL – Bitly

import pyshorteners

s = pyshorteners.Shortener()
 
#Chilp.it
s.chilpit.short('http://www.google.com')    # gives output -> 'http://chilp.it/TEST'
s.chilpit.expand('http://chilp.it/TEST')
 
#Adf.ly
s = pyshorteners.Shortener(api_key='YOUR_KEY', user_id='USER_ID', domain='test.us', group_id=12, type='int')
s.adfly.short('http://www.google.com')    # gives output -> 'http://test.us/TEST'
 
#Git.io
s = pyshorteners.Shortener(code='12345')
s.gitio.short('https://github.com/TEST')     # gives output -> 'https://git.io/12345'
s.gitio.expand('https://git.io/12345')
 
#And many more services are supported
