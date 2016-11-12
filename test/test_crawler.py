import requests, re
from bs4 import BeautifulSoup

call_url = ''
_items = set()
def spider(temp_url, entity_users):
        call_url = temp_url
        url = temp_url;
        if (temp_url not in _items):
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            # print(soup)
            for link in soup.select('a'):
                    href = link.get("href")
                    if(chkCallUrl(href, entity_users)):
                            if(href not in _items):
                                if (bool(re.search("http://blog.naver.com/" + entity_users.getId + "/*[0-9]", href))):
                                    _items.add(href)
                                if(href.find('http://')  > -1 or href.find('https://') > -1):
                                    spider(href, entity_users)
                                else:
                                    spider('http://blog.naver.com' + href, entity_users)
def chkCallUrl(href, entity_users):
    if(None == href): #null 처리
        return False
    elif(href.find('#') > -1):
        return False
    elif(href.find('javascript:') > -1):
        return False
    elif(href.find(entity_users.getId) == -1):
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

    def setItems(self, value):
        self._items.add(value)

    def getItems(self):
        return _items


def spider2(temp_url, entity_users):
                url = temp_url
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.select("frameset > frame"):
                        src = link.get("src")
                        if 'http://blog.naver.com' + src not in _items:
                            # if (bool(re.metch("http://blog.naver.com/" + entity_users.getId + "/*[0-9]", href))):
                            _items.add('http://blog.naver.com' + src)
                            spider('http://blog.naver.com' + src, entity_users) # users 객체의 공유 부분 궁금~


