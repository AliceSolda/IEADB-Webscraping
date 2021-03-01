import requests
from bs4 import BeautifulSoup
import pandas



treaty_dates = {}
treaty_members = {}


list_treaty = [

#insert list of treaty IDs here

]

i=1
n=len(list_treaty)
inc = 0

while i <= n:

    treaty_id = list_treaty[inc]

    url_string='https://iea.uoregon.edu/members/'+str(treaty_id)

    website_url=requests.get(url_string).text

    soup = BeautifulSoup(website_url,'lxml')

    my_table = soup.find(id='membership_wide_form_table')
    #print(my_table)

    #we first create a dictionnary that contains the list of nb of members for the
    # dates for which we have data, for a specific treaty.

    members = my_table.findAll('tr',{'class':"even"}) #find all the rows of the class "even"

    if len(members) > 0: #if the list of rows is empty, move on to the next treaty
        cells = members[0].findAll('td',{'class':"member-total"})
        #print(cells)
        if len(cells) > 1:
            list_members = [float(c.text) for c in cells[1:]]
            #print(list_members)

        treaty_members[treaty_id] = list_members


        #we then create a dictionnary that contains the list of dates for which we have
        # data for a specific treaty.

        dates = my_table.findAll('thead') #find all the columns heads
        #print(dates)

        list_dates = []
        for date in dates:
            cells = date.findAll('th',{'class':""})
            #print(cells)
            if len(cells) > 1:
                list_dates = [int(c.text) for c in cells[1:]]
                #print(list_dates)

        treaty_dates[treaty_id] = list_dates


    i += 1
    inc += 1

#print(treaty_members)
#print(treaty_dates)

    
##Transform dictionnary into dataframe

#We first create an excel file that contains the dates for which we have data for each treaty
max_length = max(len(m) for m in treaty_dates.values())
treaty_dates = {k: m + [""] * (max_length - len(m)) for k, m in treaty_dates.items()}
pandas.DataFrame.from_dict(treaty_dates, orient='index').to_csv(r'C:\Users\alice\Desktop\dates.csv')


#We then create an excel file that contains the nb of members for each treaty
max_length = max(len(m) for m in treaty_members.values())
treaty_members = {k: m + [""] * (max_length - len(m)) for k, m in treaty_members.items()}
pandas.DataFrame.from_dict(treaty_members, orient='index').to_csv(r'C:\Users\alice\Desktop\members.csv')



