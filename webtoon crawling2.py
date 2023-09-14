import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status() # 오류 시 종료

soup = BeautifulSoup(res.text, 'lxml')

ranks = soup.find('ul',{'class':'AsideList__content_list--FXDvm'}).find_all('li')
print(ranks)

#처음부터 다 완성된 코드 말고 간단하게 값을 확인하려고도 시도했으나 똑같이 find_all 에서 에러가 발생함
#찾아본 정보들과 비교해보면 'ul' 요소 내에 또 다른 요소가 'li'요소를 가지고 있는 형태인데 지금은 그냥 'ul'요소 안에 'li'요소들이 있는 형태로 사이트가 바뀜
#인터넷에서도 찾아보고 GPT를 활용해보아도 문제가 해결되지 않는 시행착오를 겪음
