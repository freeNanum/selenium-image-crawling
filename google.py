from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("./chromedriver", options = options)
driver.maximize_window() 
 
#"Google"에 접속한다
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
 
#페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
assert "Google" in driver.title
#assert "Naver" in driver.title
 
#검색 입력 부분에 커서를 올리고
#검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
elem = driver.find_element_by_name("q")
elem.send_keys("키워드") 
elem.submit()


prev_height = driver.execute_script("return document.body.scrollHeight")
# 웹페이지 맨 아래까지 무한 스크롤
while True:
    # 스크롤을 화면 가장 아래로 내린다
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(2)

    # 현재 문서 높이를 가져와서 저장
    curr_height = driver.execute_script("return document.body.scrollHeight")
    if(curr_height == prev_height):
        try:
            driver.find_element_by_css_selector(".mye4qd".click())
        except:
            break
    prev_height = curr_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        #imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.close()


# #입력 부분에 default로 값이 있을 수 있어 비운다
# elem.clear()
 
# #검색어를 입력한다
# elem.send_keys("Selenium")
 
# #검색을 실행한다
# elem.submit()
# #elem.send_keys("Keys.RETURN")

# #검색이 제대로 됐는지 확인한다
# assert "No results found." not in driver.page_source
 
# #브라우저를 종료한다
# #driver.close()

