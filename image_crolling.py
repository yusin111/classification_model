# 데이터의 형태
# 1. 정형데이터 - 일정한 규칙으로 구성된 데이터, DB...
# 2. 반정형데이터 - 규칙은 없지만 구조를 갖춘 데이터, xml,json,html...
# 3. 비정형데이터 - 규칙과 규격구조가 존재하지 않는 데이터, SNS,동영상,이미지,음성,텍스트...
from selenium import webdriver # 기본 드라이버
from selenium.webdriver.common.keys import Keys # 키 전송
from selenium.webdriver.common.by import By # 선택자
from urllib import parse,request
import time
import requests
import os

driver = webdriver.Chrome()
driver.get("https://www.google.com") # 페이지 요청 > driver 페이지 파일이 저장
driver.implicitly_wait(0.5)
#print(dir(driver))
#print(driver.page_source)

img = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/img")
imgsrc = (img.get_attribute("src"))
res = requests.get(imgsrc)
# print(dir(res))
# print(res.content)
with open("saveimg/test.png","wb") as fp:
    fp.write(res.content)


time.sleep(600)