import requests
from bs4 import BeautifulSoup

call_url = ''
items = set()
def spider(temp_url):
        call_url = temp_url
        url = temp_url;
        if (temp_url not in items):
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            # print(soup)
            for link in soup.select('a'):
                    href = link.get("href")
                    if(chkCallUrl(href)):
                            if(href not in items):
                                items.add(href)
                                if(href.find('http://')  > -1 or href.find('https://') > -1):
                                    spider(href)
                                else:
                                    spider('http://blog.naver.com' + href)
def chkCallUrl(href):
    if(None == href): #null 처리
        return False
    elif(href.find('#') > -1):
        return False
    elif(href.find('javascript:') > -1):
        return False
    elif(href.find(users_1.getId) == -1):
        return False
    else:
        return True

#setter getter
class users():
    def __init__(self):
        self._id = None

    @property
    def getId(self):
        print(self._id)
        return self._id

    def setId(self, value):
        self._id = value


def spider2(temp_url):
                url = temp_url
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.select("frameset > frame"):
                        src = link.get("src")
                        # print(src)
                        if 'http://blog.naver.com' + src not in items:
                            items.add('http://blog.naver.com' + src)
                            spider('http://blog.naver.com' + src)


