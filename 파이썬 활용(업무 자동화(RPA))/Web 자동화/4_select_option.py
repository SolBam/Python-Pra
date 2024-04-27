import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# cars에 해당하는 element를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[4]')
# elem.click()

# 텍스트 값을 통해서 선택하는 방법
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택하는 방법
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(5)

browser.quit()