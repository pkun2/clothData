#https://kream.co.kr/search?category_id=64&category_id=65
import requests
from db import dbConect, insertDB
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def coupang():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
    
    url = "https://www.coupang.com/np/search?component=&q=%EC%98%B7&channel=user" #크롤링할 사이트
    #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"} #403 에러 수정

    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, "lxml") #lxml형태로 불러옴

    coll_name = "coupang"
    dbConect()
    
    for i in range(2, 10):
        time.sleep(1)
        
        if(i==2 or i > 6):
            page_xpath = '//*[@id="searchOptionForm"]/div[2]/div[2]/div[5]/span[2]/a[' + str(i) + ']'
        else:
            page_xpath = '//*[@id="searchOptionForm"]/div[2]/div[2]/div[5]/span[1]/a[' + str(i) + ']'
            
        cloth_list = soup.select("#searchOptionForm > div.search-wrapper > div.search-content.search-content-with-feedback > ul > li") #리스트 데이터     
    
        for cloth in cloth_list:
            name = cloth.select_one("#searchOptionForm > div.search-wrapper > div.search-content.search-content-with-feedback > ul > li > a > dl > dd > div > div.name").text #무신사 옷의 제목 가져오기
            rate = cloth.select_one("#searchOptionForm > div.search-wrapper > div.search-content.search-content-with-feedback > ul > li > a > dl > dd > div > div.other-info > div > span > em").text
            
            document = {"name": name, "rate": rate}
            insertDB(document, "bigdata", coll_name)
            
            
        driver.find_element(By.XPATH, page_xpath).click()
        print(i-1)
            
    print(coll_name + "done")
        
    driver.close()