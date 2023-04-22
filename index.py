import requests
from bs4 import BeautifulSoup

url = "https://www.musinsa.com/categories/item/002" #크롤링할 사이트
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"} #403 에러 수정

response = requests.get(url, headers=headers)  # 데이터 가져오기
response.raise_for_status() #http 오류 발생 검증 코드

soup = BeautifulSoup(response.text, "lxml") #lxml형태로 불러옴


cloth_list = soup.select("#searchList > li") #리스트 데이터 

for cloth in cloth_list:
    name = cloth.select_one("#searchList > li >  div.li_inner > div.article_info > p.list_info > a")["title"] #무신사 옷의 제목 가져오기
    print(name)

#searchList > li:nth-child(1) > div.li_inner > div.article_info > p.list_info > a
#searchList > li:nth-child(1)