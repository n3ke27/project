from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
from lxml import etree

def get_page_content(url, head):

  req = Request(url, headers=head)
  return urlopen(req)


def get_news():
    file = open("test2.txt", 'w')
    url = 'https://www.hltv.org/'
    head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'refere': 'https://example.com',
    'cookie': """your cookie value ( you can get that from your web page) """
    }
    page = get_page_content(url, head)
    html_code = page.read().decode('utf-8')

    soup = BeautifulSoup(html_code, 'html.parser')
    names = set()
    l = soup.find('a', class_='newsline article').get('href')
    if l != None:
        return 'hltv.org'+l


