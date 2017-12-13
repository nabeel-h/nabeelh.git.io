from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from bs4 import NavigableString
from time import sleep
import csv



print('BEGINNING')
sleep(10)
my_url = 'https://www.reddit.com/r/nba/'
sleep(10)
uClient = uReq(my_url)
sleep(10)
page_html = uClient.read()
sleep(10)
uClient.close()
print('OPENING REDDIT')
sleep(10)
print('WAITING TO LOAD INTO SOUP')
sleep(10)
page_soup = soup(page_html, 'html.parser')
print('WAITING TO LOAD VALUES INTO LIST')
sleep(10)

#pulls list of subreddit links from top of page
subreddit_soup = page_soup.findAll('div',{'class':'md'})[0].findAll('ul')[1]

teams = {}

#loops through subreddit links and pulls values
for child in subreddit_soup:
	
	
	if isinstance(child, NavigableString): continue
	sub_name = child.a['href']
	sub_name = sub_name[3:]
	team_name = child.get_text()
	
	teams[team_name] = sub_name
	
with open('nba_reddit_subnames.csv','w',newline='') as f:
	w = csv.writer(f)
	for key,value in teams.items():
	 w.writerow([key,value])
	
	

	

	

