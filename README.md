# 1주차 크롤링

1. 목표 사이트

네이버 웹툰의 실시간 인기 순위를 크롤링하는 코드를 작성하는 것이 목표

2. 내가 공부한 크롤링 기법

- BeautifulSoup을 이용한 크롤링 코드

      import requests
      from bs4 import BeautifulSoup

      url = "https://news.naver.com/main/ranking/popularMemo.naver"
      headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}

      res = requests.get(url, headers=headers)
      soup = BeautifulSoup(res.text, 'lxml')

- selenium을 이용한 크롤링 코드(동적 웹 크롤링)

      from selenium import webdriver

      driver = webdriver.Chrome('/path/to/chromedriver')

      driver.get('https://news.google.com')

      titles = driver.find_elements_by_xpath("//a[@class='DY5T1d']")
      for title in titles:
      print(title.text)
      print(title.get_attribute('href'))

      driver.quit()


3. 목표 사이트에 접근하기 위해 작성한 코드 & 수정

-빈 파일을 만들고 크롤링을 한 후 파일 안에 크롤링한 데이터를 넣어서 네이버 윕툰 인기 순위 데이터를 가져오는 코드

      import csv
      import requests
      from bs4 import BeautifulSoup

      url ="https://comic.naver.com/index"

      filename = "네이버 웹툰 인기 순위.csv"
      f = open(filename, "w", encoding="utf-8-sig", newline="")
      writer = csv.writer(f)

      columns_name = ["순위", "웹툰명"]

      writer.writerow(columns_name)

      res = requests.get(url)
      res.raise_for_status()

      soup = BeautifulSoup(res.text, "lxml")
      cartoonsBox = soup.find('ul', attrs={"class": "AsideList__content_list--FXDvm"})
      cartoons = cartoonsBox.find_all('span')
      i = 1

      for cartoon in cartoons: 
          title = cartoon.get("span.text") 
          print(f"{str(i)}위: {title}")
          data = [str(i), title]
          writer.writerow(data)
          i += 1

- cartoonsBox.find_all('span') 에서 find_all 부분에서 에러가 발생함. 그래서 처음 불러오는 부분만 다시 코딩하고 실행.

      import requests
      from bs4 import BeautifulSoup

      url = "https://comic.naver.com/index"
      res = requests.get(url)
      res.raise_for_status() # 오류 시 종료

      soup = BeautifulSoup(res.text, 'lxml')

      ranks = soup.find('ul',{'class':'AsideList__content_list--FXDvm'}).find_all('li')
      print(ranks)
  
처음부터 다 완성된 코드 말고 간단하게 값을 확인하려고도 시도했으나 똑같이 find_all 에서 에러가 발생함.

찾아본 정보들과 비교해보면 'ul' 요소 내에 또 다른 요소가 'li'요소를 가지고 있는 형태인데 지금은 그냥 'ul'요소 안에 'li'요소들이 있는 형태로 사이트가 바뀜.

인터넷에서도 찾아보고 GPT를 활용해보아도 문제가 해결되지 않음.

4. 최종

찾아보니 오류가 나는 이유가 저작권과 관련된 문제때문에 발생한다는 것이 가장 확률이 높음.
그래도 이번에 크롤링 코드를 짜면서 여러가지 크롤링 기법들을 공부하고 사이트의 구조를 파악하는 등 다양한 실무적인 경험을 통해
처음보는 코드가 나오더라도 빠르게 정보를 찾고 이해하고 적용하는 과정을 학습했음.


