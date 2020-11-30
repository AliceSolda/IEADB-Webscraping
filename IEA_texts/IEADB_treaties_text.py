import requests
import urllib.request
import re
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
    html_treaty = soup.find('div', {'class':'content clearfix'})
    text_treaty = str(html_treaty)  

    filename = "text_"+str(treaty)
    print(filename) #print the file name to test that the code is working
    location = "C:/Users/alice/Desktop/treaties/" + filename + ".doc"
    file = open(location, "w", encoding="utf-8")

    #Now we are going to clean our text from its HTML tags and write the 
    #"clean" text in our word document.
    
    cleanr = re.compile('<.*?>')
    clean_text = re.sub(cleanr, '', text_treaty)
    file.write(clean_text)    
    file.close()
