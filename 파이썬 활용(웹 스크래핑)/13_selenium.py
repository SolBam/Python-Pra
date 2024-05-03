import time
from selenium import webdriver

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_id_name("account")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("네이버 아이디")
browser.find_element_by_id("pw").send_keys("네이버 비밀번호")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id를 새로 입력
# browser.find_element_by_id("id").send_keys("새로운 네이버 아이디")
browser.find_element_by_id("id").clear() # 전에 입력했던 입력 값을 지움
browser.find_element_by_id("id").send_keys("새로운 네이버 아이디")

# 6. html 정보 출력
print(browser.page_source)

# 7. Browser 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 Browser 종료

# elem = browser.find_element_by_class_name("link_login")
# elem.click() # 선택한 태그를 클릭
# browser.back() # 뒤로가기
# browser.forward() # 앞으로
# browser.refresh() # 새로고침

# elem1 = browser.find_element_by_id("query")
# elem1.send_keys("나도코딩") # 선택한 태크에 글을 입력
# elem1.send_keys(Keys.ENTER) # ENTER 키를 대신해서 사용가능

# elem2 = browser.find_elements_by_tag_name("a") # 선택한 태그를 모두 불러옴
# elem2.get_attribute("href") # a 태그에 해당하는 href 태그를 모두 불러옴

# browser.get("http://daum.net")
# elem3 = browser.find_element_by_name("q")
# elem3.send_keys("나도코딩") # 태그 위치에 글을 입력

# browser.close() # 현재 열려있는 탭만 닫힘
# browser.quit() # 전체 창을 닫음