# Imports the requests library.
import requests
import re
import json
# Import Beautiful soup library
from bs4 import BeautifulSoup

'''
This url is a local path to your html file, 
replace the url to your specific html file.
'''

url = "D:\Python_notebook\/realtor.html"
page = open(url)

# This will parse the html into r object
soup = BeautifulSoup(page.read(), 'html.parser')

output = {}

# For Name
y = soup.find_all("font", {'class': "font16"})
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
with open("output.json", "w") as kekw:
    json.dump(output, kekw)
