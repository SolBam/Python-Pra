웹 스크래핑 용어 정리

HTML : 뼈대
CSS : 예쁘게
Java Script : 살아있게
XPath : Element의 경로

정규식 : 규칙을 가진 문자열을 표현하는 식
. : 하나의 문자
^ : 문자열의 시작
$ : 문자열의 끝
match() : 처음부터 일치하는지
search() : 일치하는 게 있는지
findall() : 일치하는 것 모두 리스트로

User-Agent : 사람이 맞는지 확인

Requests : 웹 페이지(HTML) 읽어오기
    - 빠르다, 동적 웹 페이지 X
    - 주어진 URL을 통해 받아온 HTML에 원하는 정보가 있을 때
    
Selenium : 웹 페이지 자동화
    - 느리다, 동적 웹 페이지 O
    - 로그인, 어떤 결과에 대한 필터링 등 어떤 동작을 해야 하는 경우
    - 크롬 버전에 맞는 chromedriver.ex가 반드시 있어야 한다.
    - find_element(s)_by_id : id로 찾기
      find_element(s)_by_class_name : class name 으로 찾기
      find_element(s)_by_link_text : 링크 text로 찾기
      find_element(s)_by_xpath : xpath로 찾기
      click() : 클릭
      send_keys() : 글자 입력
      clear() : 글자 지움
      
BeautifulSoup : 원하는 데이터 추출(웹 스크래핑)
    - find : 조건에 맞는 첫 번째 element
      find_all : 조건에 맞는 모든 element 리스트로
      find_next_sibling(s) : 다음 형제 찾기
      find_previous_sibling(s) : 이전 형제 찾기
      soup["href"] : 속성
      soup.get_text() : 텍스트

이미지 다운로드 : with open("파일명", "wb") as f: f.write(res.content)

CSV : import csv   f = open(filename, "w", encoding="utf-8-sig", newline="")

Headless Chrome : 브라우저를 띄우지 않고 동작
    - 때로는 User-Agent 정의 필요
    - 59버전부터(최신 버전이면 모두 가능)

무분별한 웹 크롤링 / 웹 스트래핑은 대상 서버에 부하 -> 계정 / IP 차단
데이터 사용 주의 -> 이미지, 텍스트 등 데이터 무단 활용 시 저작권 등 침해 요소, 법적 제재
robot.txt -> 법적 효력 X, 대상 사이트의 권고