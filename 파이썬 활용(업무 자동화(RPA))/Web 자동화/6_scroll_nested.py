import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)

# 특정 영역 스크롤
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[65]')

# 방법 1: ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2: 좌표 정보 이동
# xy = elem.location_once_scrolled_into_view # 함수가 아닌 변수
# print("type : ", type(xy)) # dict
# print("value : ", xy)

elem.click()

time.sleep(5)
browser.quit()