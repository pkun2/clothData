#https://kream.co.kr/search?category_id=64&category_id=65
import requests
from db import dbConect, insertDB
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def naver():
    driver = webdriver.Chrome('chromedriver')
    
    url = "https://search.shopping.naver.com/search/all?query=%EC%98%B7&cat_id=&frm=NVSHATC&pagingSize=100" #크롤링할 사이트
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"} #403 에러 수정

    driver.get(url)
    
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    
    soup = BeautifulSoup(driver.page_source, "lxml") #lxml형태로 불러옴

    coll_name = "naver"
    dbConect()
    
    for i in range(1, 9):
        page_xpath = '//*[@id="content"]/div[1]/div[4]/div/a[' + str(i) + ']'

        cloth_list = soup.select("#content > div.style_content__xWg5l > div.list_basis > div > div") #리스트 데이터 
        
        for cloth in cloth_list:
            name = cloth.select_one("#content > div.style_content__xWg5l > div.list_basis > div > div > div > div > div.basicList_info_area__TWvzp > div.basicList_title__VfX3c > a")["title"] #무신사 옷의 제목 가져오기
            jjim = cloth.select_one("#content > div.style_content__xWg5l > div.list_basis > div > div > div > div > div.basicList_info_area__TWvzp > div.basicList_etc_box__5lkgg > span > a > span > em").text
            
            document = {"name": name, "jjim": jjim}
            insertDB(document, "bigdata", coll_name);
            
        driver.find_element(By.XPATH, page_xpath).click()
        time.sleep(2)
        
        print(i)
        
    print(coll_name + "done")
    
    driver.close()