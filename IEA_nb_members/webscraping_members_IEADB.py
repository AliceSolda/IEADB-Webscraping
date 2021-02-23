import requests
from bs4 import BeautifulSoup
import re
import pandas 



treaty_dates = {}
treaty_members = {}


list_treaty = [

    #add all treaties IDs in there
   
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

    all_tr = my_table.findAll('tr',{'class':"even"}) #find all the rows of the class "even"
    if all_tr: #if the list of rows is empty, move on to the next treaty
        members = []
        members.append(all_tr[0])
        print(members)

        list_members = []
        for member in members:
            cells = member.findAll('td',{'class':"member-total"})
            del cells[0]
            str_cells = str(cells)
            clean = re.compile('<.*?>')
            clean2 = (re.sub(clean, '',str_cells))
            if clean2 != "[]":
                list_members.append(clean2)

        #print(list_members)

        treaty_members[treaty_id] = list_members


        #we then create a dictionnary that contains the list of dates for which we have
        # data for a specific treaty.

        dates = my_table.findAll('thead') #find all the columns heads
        #print(dates)

        list_dates = []
        for date in dates:
            cells = date.findAll('th',{'class':""})
            del cells[0]
            str_cells = str(cells)
            clean = re.compile('<.*?>')
            clean2 = (re.sub(clean, '',str_cells))
            if clean2 != "[]":
                list_dates.append(clean2)

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



