# Imports the requests library.
# Imports regex library.
# Imports json library.
# Imports BeautifulSoup library.

import requests
import re
import json
from bs4 import BeautifulSoup

'''
This url is a local path to your html file, 
replace the url to your specific html file path.
'''

url = "D:\Python_notebook\/realtor.html"
page = open(url)

# This will parse the html into soup object
soup = BeautifulSoup(page.read(), 'html.parser')

output = {}

# For Name
y = soup.find_all("font", {'class': "font16"})

# Loop finds the instances strong inside y.
for i in y:
    z = i.find('strong')
    if z:
        q = z.get_text()
output["name"] = q

# For Email
x = soup.find_all("a", {'href': re.compile(r'^mailto:')})
temp = []
for i in x:
    temp.append(i.get_text())
output["Email"] = temp[1]

# For Phone number
z = soup.find_all("a", {'href': re.compile(r'^tel:')})
temp2 = []
for i in z:
    temp2.append(i.get_text())
output["Phone"] = temp2[0]
print(output)

# Runs as a function like a loop, and closes file operation
# Creates a json output file.
with open("output.json", "w") as full:
    json.dump(output, full)
