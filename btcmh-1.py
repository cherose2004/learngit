#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    # try:
    r = requests.get(url, timeout = 60)
    r.raise_for_status()
    html = r.text
    Soup = BeautifulSoup(html,"lxml")
    tr = Soup.find_all("tr")
    for td in tr:
        data = td.find_all("td")
        if len(data)>=5: 
            # print(data)
            print(data[0].string,"--->",data[3].string)
            print("***")
    return None

    # except:
        # print('something wrong!')
        # return ""

def main():
    url="http://www.bjzhongyi.com/jzzn/article/7020.html"
    HTML=getHTMLText(url)



if  __name__ == "__main__":
    main()
