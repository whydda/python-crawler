import requests
from bs4 import BeautifulSoup

def spider():
        url = 'http://blog.naver.com/whydda'
        source_code = requests.get(url)
        plain_text = source_code.text
        #soup = BeautifulSoup(plain_text, 'lxml')
        print(plain_text)
spider()