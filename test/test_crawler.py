import requests
from bs4 import BeautifulSoup

def spider(temp_url):
        url = temp_url;
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        # print(soup)
        for link in soup.select('p > a'):
                href = link.get("href")
                if(href != '#'):
                        if(str(href).find("http://blog.naver.com/whydda") > -1):
                            print(href)
                            spider2(href)


def spider2(temp_url):
        url = temp_url;
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.select("frameset > frame"):
                src = link.get("src")
                print(src)
                if (str(src).find("/NBlogHidden.nhn?blogId=whydda&musicYN=false") < 0):
                        spider('http://blog.naver.com' + src)

spider('http://blog.naver.com/PostList.nhn?blogId=whydda&widgetTypeCall=true')
