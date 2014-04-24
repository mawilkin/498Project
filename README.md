OPINION ENGINE by TEAM #SENTIMENT  
=================================  
  
EECS 498 Final Project, extracting emotion from the web.  
  
  {mawilkin, mkriete, parisedj, pdubslax} @ umich.edu  

Problem  
=======  
Human analysis of content takes a long time, and its difficult to extract the emotion from a set of web texts. We seek to take advantage of aggregated, user created web content to determine the general feeling of a given topic on the web.  

Solution  
========  
Our web-based opinion engine operates as a web server that takes a query as input. We then use the Alchemy API to extract the primary subject of the query. With this subject, we perform a searches on bing and twitter to gather a real-time result set, which we then analyze.  

Dependencies  
============  
  
 - Requests  -- http://docs.python-requests.org/  
 - Beautiful Soup 4  -- http://www.crummy.com/software/BeautifulSoup/  
  
  
How to build  
============  
Install dependencies 
  
How to run  
==========  
python server.py  -- This starts the server on port 3000

browser to http://localhost:3000/input.html  

Input a query.  
  
