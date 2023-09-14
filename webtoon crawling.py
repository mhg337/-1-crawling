
#네이버 웹툰의 실시간 인기웹툰 정보를 크롤링하는 코드를 만들려고 했습니다.

# 라이브러리 준비
import csv
import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/index"

# 엑셀 파일로 저장하기
filename = "네이버 웹툰 인기 순위.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_name = ["순위", "웹툰명"] # 컬럼 속성명 만들기

writer.writerow(columns_name)

# 웹 서버에 요청하기
res = requests.get(url)
res.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(res.text, "lxml")
cartoonsBox = soup.find('ul', attrs={"class": "AsideList__content_list--FXDvm"}) # 전체 영역에서 'span' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한
cartoons = cartoonsBox.find_all('span') # 인기 급상승 영역에서 'span'태그 모두 찾아 변수 cartoons에 할당
i = 1

# 반복문으로 제목 가져오기(터미널 창 출력 및 엑셀 저장)
for cartoon in cartoons: 
  title = cartoon.get("span.text") 
  print(f"{str(i)}위: {title}")
  data = [str(i), title]
  writer.writerow(data)
  i += 1

#하지만 26,27번째 줄에서 cartoonsBox 함수에 값이 None으로 뜨면서 find_all 부분에서 오류가 계속 발생하여 ul이나 span이라는 요소가 있는지 class속성을 제대로 입력하였는지
#계속 확인하였지만 결국 해결되지 않아 다른 코드로 시도해 보았지만 어떤 원인이 에러를 야기하는지 발견하지 못해 이론만 이해하고 실제로 크롤링을 해보지는 못했습니다.
