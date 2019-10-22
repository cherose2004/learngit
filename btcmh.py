#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 60)
        r.raise_for_status()
        s = json.loads(r.text)
        html = s.get('html')
        return html
    except:
        print('timeout!')
        return ""

def main():
    url="http://www.bjzhongyi.com/jzzn/article/7020.html"
    HTML=getHTMLText(url)
    print(HTML)



if  __name__ == "__main__":
    main()
