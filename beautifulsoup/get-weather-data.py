import urllib2
from bs4 import BeautifulSoup


#create/open a file
f = open("weatherdata.txt", "w");


#Months January to December
for m in range(1,13):

# First to last day of the month
    for d in range(1,32):
        if (m==2 and d>28):
            break
        elif(m in [4,6,9,11] and d>30):
            break

        timestamp = '2009 ' + str(m) + ' ' + str(d)
        print "getting data for "+ timestamp


#open the webpage
        url = 'http://www.wunderground.com/history/airport/KBUF/2009' + '/'+ str(m) + '/' + str(d) +'/DailyHistory.html'


#general data scrape

        page = urllib2.urlopen(url)

#soupify it
        soup = BeautifulSoup(page)

        data = soup.findAll(attrs={"class":"wx-value"});

        print data[0].contents[0]

        f.write(timestamp + ' - ' + data[0].contents[0] + '\n')



