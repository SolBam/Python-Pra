import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

# url 접속
browser.get('https://www.w3schools.com/')

# LEARN HTML 클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# HOW TO 클릭
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]').click()

# Contact Form 메뉴 클릭
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()
# browser.find_element_by_link_text('Contact Form').click() # Contact Form이 2개 이상의 링크 텍스트가 있는 경우 실패
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # 가장 좋은 방법
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click() # 일부 텍스트 비교

# 입력란에 아래 값 입력
first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
browser.find_element(By.XPATH, '//*[@id="country"]/option[2]').click()
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

# 5초 대기 후 브라우저 종료
time.sleep(5)
browser.quit()