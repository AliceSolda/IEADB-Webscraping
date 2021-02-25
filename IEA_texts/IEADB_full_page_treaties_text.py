import requests
import urllib.request
from bs4 import BeautifulSoup


list_treaty = [
    
#add all treaties IDs in there

    ]

for treaty in list_treaty: 
    url_string='https://iea.uoregon.edu/treaty-text/'+str(treaty)
    print(url_string) #print the URL to test that the code is working
    
    website_url=requests.get(url_string).text

    soup = BeautifulSoup(website_url,'lxml')

    filename = "text_"+str(treaty)
    print(filename) #print the file name to test that the code is working
    location = "C:/Users/alice/Desktop/treaties/" + filename + ".doc"
    file = open(location, "w", encoding="utf-8")
    file.write(str(soup))    
    file.close()
