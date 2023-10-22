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

5. 최종



