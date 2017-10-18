from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from bs4 import NavigableString
import sqlite3
from time import sleep

#sql db section
conn = sqlite3.connect('reddit_db.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS NBA_subs''')

cur.execute('''
CREATE TABLE IF NOT EXISTS NBA_subs(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	sub_name TEXT UNIQUE,
	team_name TEXT UNIQUE
)''')



print('BEGINNING')
sleep(10)
my_url = 'https://www.reddit.com/r/nba/'
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


#loops through subreddit links and pulls values
for child in subreddit_soup:
	if isinstance(child, NavigableString): continue
	sub_name = child.a['href']
	sub_name = sub_name[3:]
	team_name = child.get_text()
	
	cur.execute('''INSERT INTO NBA_subs (sub_name,team_name) VALUES (?,?)''',(sub_name,team_name))
	
conn.commit()
	

	

	

