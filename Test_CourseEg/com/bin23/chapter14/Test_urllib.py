import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

# soup = BeautifulSoup("html_doc")
# type(soup)
# print(soup)

params = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon':0}).encode()
f = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?" % params)
print(f.getcode())
