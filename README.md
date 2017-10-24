# nabeel-h/port.io

This is a repo that will be used to store some personal data analysis projects.


### reddit NBA community analysis:

[Link to Jupyter notebook](https://github.com/nabeel-h/port.io/blob/master/Notebooks/nba_reddit/Reddit%20NBA%20Subreddit%20Analysis.ipynb)

This analysis takes a look at NBA community on the popular social media website [reddit.com](https://www.reddit.com).
There are 32 teams in the NBA and as a result 33 subreddits (micro-communities): one for each [team](https://www.reddit.com/r/lakers) with an additional one for the [NBA](https://www.reddit.com/r/nba) itself.

The analysis looks into the growth of the community and other interesting facts.

Data was obtained through an API over the course of a couple of days and the data was stored in a sqlite3 database.
A python data stack was used for analysis and data manipulation.

The following python libraries were used: PRAW (reddit api wrapper), pandas, numpy, matplotlib,sqlite3
Database: sqlite3


### Makeup of NBA player positions from 1977 to 2017:

[Link to Jupyter notebook](https://github.com/nabeel-h/port.io/blob/master/Notebooks/bballref_NBApositions/bbrallref_NBA_Position_analysis.ipynb)

I was wondering how the make up of the NBA by player position had evolved over time. For example what % of the league played the PG position in 1980? What % of the league in 2017 are point guards? This was interesting to me because NBA schemes now are very different from the past and as a result I expected the composition of positions to reflect this.

Since this information is not a readily available NBA stat I calculated this information by extracting NBA historical data from [basketball-reference.com](https://www.basketball-reference.com). 

The following python libraries were used: BeautifulSoup4 (for parsing HTML data), pandas, numpy, matplotlib

