#구글 모듈
import os.path
#사자,호랑이,곰,앵무새,개구리,표범,독수리,코끼리,타조,말
#lion,tiger,bear,parrot,frog,leopard,eagle,elephant,ostrich,horse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains
import time
from urllib import request,parse
import uuid

def get_google(search_datas,save_directory,cnt_count):
    for searchKeyword,keyword in search_datas:
       searchKeyword =searchKeyword .strip()
       keyword = keyword.strip()
       time.sleep(5)
       driver = webdriver.Chrome()
       driver.get("https://images.google.com/?hl=ko")
       f_ele = driver.find_element(By.CSS_SELECTOR,"[title=검색]")
       #print(f_ele.tag_name)
       f_ele.send_keys(searchKeyword)
       f_ele.send_keys(Keys.ENTER)
       driver.implicitly_wait(1)
       #구글 이미지는 마우스 오버링 후에 주소가 생성된다.
       # 전체 페이지 로딩
       time.sleep(2)
       driver.fullscreen_window()
       sfooter = driver.find_element(By.CSS_SELECTOR,"#sfooter");
       cnt=0
       for i in range(100):
           cnt += 50
           if cnt >= cnt_count:
               break
           ActionChains(driver).send_keys(Keys.END).perform()
           time.sleep(2)
           if not "none" in sfooter.get_attribute("style"):
               break
       over_tar = driver.find_elements(By.CSS_SELECTOR,f"[data-q={searchKeyword}] g-img")
       # print(len(over_tar))
       cnt=0
       for target in over_tar:
           if int(cnt*0.5) > cnt_count:
               break
           cnt+=1
           ActionChains(driver).move_to_element(target).perform()
           print(".",end="")
           time.sleep(0.3)
       #a href="/imgres?q=
       print()
       result_url = (
           driver.find_elements(By.CSS_SELECTOR,\
                                f"[data-q={searchKeyword}] a[href*=imgres]"))
       import re
       pattern = r".*imgurl=(.*)&imgrefurl.*"
       iurls=[]
       for iurl in result_url:
           iurls.append(re.sub(pattern, r"\1", iurl.get_attribute("href")))
       #print(parse.unquote(iurls[0]))  %XX => url 문자를 일반 전환
       save_path = f"{save_directory}\\{keyword}\\"
       if not os.path.exists(save_path):
           os.mkdir(save_path)
       icount=0
       for iurl in iurls:
           try:
               img_url = (
                   re.findall(r"(.*\.jpg|.*\.JPG|.*\.jpeg|.*\.JPEG|.*\.png|.*\.PNG|.*\.webp|.*\.WEBP)$",iurl))[0]
               img_url = parse.unquote(img_url)
               expandfile = img_url.split(".")[-1]
               ru = "g"+str(uuid.uuid4())
               file_path=ru+"."+expandfile
               datafile = requests.get(img_url)
               time.sleep(0.7)
               #print((datafile.headers["content-length"])) 파일 용량 byte
               if int(datafile.headers["content-length"])<5100:
                   continue
               #request.urlretrieve(img_url,save_path+file_path)
               with open(save_path+file_path,"wb") as fp:
                   fp.write(datafile.content)
                   icount+=1
               if icount>=cnt_count:
                   break
           except:
               print("err")
       print("구글에서 ",icount," 개의 이미지 저장")
       driver.quit();

if __name__=="__main__":
    print("Craw_image_running 파일에서 실행하세요")