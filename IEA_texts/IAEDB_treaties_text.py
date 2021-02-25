import requests
import urllib.request
from bs4 import BeautifulSoup

#to run this code, you first need to create a folder where you will
# store the treaties texts. In this example, I created a folder 
#called "treaties" on my desktop.

list_treaty = [
    
#add all treaties IDs in there

    ]

for treaty in list_treaty: 
    url_string='https://iea.uoregon.edu/treaty-text/'+str(treaty)
    print(url_string) #print the URL to test that the code is working
    
    website_url=requests.get(url_string)

    soup = BeautifulSoup(website_url.text,'lxml')
    text_treaty = soup.find('div', {'class':'content clearfix'}).get_text()

    filename = "text_"+str(treaty)
    print(filename) #print the file name to test that the code is working
    location = "C:/Users/alice/Desktop/treaties/" + filename + ".doc"
    file = open(location, "w", encoding="utf-8")

    #Now we are going to clean our text from its HTML tags and write the 
    #"clean" text in our word document.
    
    file.write(str(text_treaty))    
    file.close()
