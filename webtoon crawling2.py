import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status() # 오류 시 종료

soup = BeautifulSoup(res.text, 'lxml')

ranks = soup.find('ul',{'class':'AsideList__content_list--FXDvm'}).find_all('li')
print(ranks)