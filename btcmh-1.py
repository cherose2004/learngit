import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    flag = 0
    r = requests.get(url, timeout = 60)
    r.raise_for_status()
    html = r.text
    Soup = BeautifulSoup(html,"lxml")
    tr = Soup.find_all("tr")
    in_name = input("输入要选择的医生姓名中的一部分：")
    print("{0:<10}{1:<8}".format("姓名","出诊时间"))
    for td in tr:
        data = td.find_all("td")
        if len(data)>=5 :
            name = str(data[0].string).replace("　","").replace(" ","").strip()
            if in_name in name:
                print("{0:<10}".format(name),end="")
                print("{0}".format(str(data[3].string).strip().replace(" ","")))
                flag = 1
    if flag == 0:
        print("无信息！")
    return None

def main():
    url="http://www.bjzhongyi.com/jzzn/article/7020.html"
    HTML=getHTMLText(url)



if  __name__ == "__main__":
    main()
