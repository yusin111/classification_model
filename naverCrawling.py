#네이버 모듈
import os.path
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains
import time
from urllib import parse
import uuid
import re


def get_naver(search_datas,cnt_count):
   for searchKeyword,keyword in search_datas:
       searchKeyword = searchKeyword.strip()
       keyword = keyword.strip()
       time.sleep(5)
       #네이버 접속
       driver = webdriver.Chrome()        #
       driver.get(r"https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={}".format(searchKeyword))
       #class = image_group 이미지 컨테이너
       # img > src 이미지 경로
       # End 키 누를때 맨 밑으로 이동하며 이미지를 가져옵니다.
       time.sleep(3)
       driver.fullscreen_window()
       cnt = 0
       for i in range(100):
           cnt += 50
           if cnt >= cnt_count:
               break
           ActionChains(driver).send_keys(Keys.END).perform()
           time.sleep(2)
       f_ele = driver.find_elements(By.CSS_SELECTOR,".image_group img")
       f_ele = f_ele[:cnt_count]
       print(len(f_ele))
       f_ele = \
           [ie.get_attribute("src") \
            for ie in f_ele if ie.get_attribute("src").startswith("http")]
       pattern = r".+src=(http.+(\.jpg|\.JPG|\.png))"
       f_url=[]
       for ele in f_ele:
           try:
               f_url.append(
                   parse.unquote(re.search(pattern=pattern,string=ele).groups()[0]))
           except:
               pass
       icount = 0
       for u in f_url:
           print(".",end="")
           img_site=requests.get(u)
           time.sleep(0.7)
           #print(img_site.headers) 동일 이미지 색출할때
           contentLength=""
           try:
               global contentLength
               contentLength =(
                       img_site.headers["Content-Length"] or img_site.headers["content-length"])
           except:
               continue
           if int(contentLength)<5100:
               continue
           simg = img_site.content
           save_path = f"d:\\imgs\\{keyword}\\"
           if not os.path.exists(r"d:\imgs"):
               os.mkdir(r"d:\imgs")
           if not os.path.exists(save_path):
               os.mkdir(save_path)
           expandfile = u.split(".")[-1]
           ru = "n"+str(uuid.uuid4())
           file_path = ru + "." + expandfile
           with open(save_path+file_path,"wb") as fp:
               fp.write(simg)
               icount+=1
       print()
       print("네이버에서 {} 개를 받았습니다.".format(icount))
       driver.quit();