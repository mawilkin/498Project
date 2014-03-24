import sys
import urllib2
from bs4 import BeautifulSoup

str = urllib2.urlopen('http://wikipedia.com/')
page = str.read()
soup = BeautifulSoup(page)
print(soup.get_text())
