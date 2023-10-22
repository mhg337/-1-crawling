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



4. 최종



