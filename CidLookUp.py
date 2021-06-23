# Look up caller ID using the numverify API!

import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for EX data
def getdata(url):
    req=requests.get(url)
    return req.text

# enter api key
api = 'YOURAPIKEYHERE'

number=input("number: ")
country=input("country(2-3 letters): ")

# pass api, num & country code
htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)