import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib
import bs4

src = input("제목 입력:")
rcs = src.replace(" ", "+")
enc_src = urllib.parse.quote(rcs)
url = 'https://www.youtube.com/results?search_query=' + enc_src
req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html, 'html5lib')
ex_first = soup.find('ytd-app')
print(ex_first)

