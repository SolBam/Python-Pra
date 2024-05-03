# 조건 1: 네이버에서 오늘 서울의 날씨정보를 가져온다.
# 조건 2: 헤드라인 뉴스 3건을 가져온다.
# 조건 3: IT 뉴스 3건을 가져온다.
# 조건 4: 해커스 어학원 홈페이지에서 오늘의 영어 회화 자문을 가져온다.

import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print(" (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    
    # 온도
    cast = soup.find("div", attrs={"class":"temperature_info"}).get_text()
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("도씨", "") # 현재 온도
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text() # 최저 온도
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text() # 최고 온도
    
    # 강수량
    morning_rain_rate = soup.find("span", attrs={"class":"weather_left"}).get_text().strip() # 오전 강수 확률
    afternoon_rain_rate = soup.find("span", attrs={"class":"weather_inner"}).get_text().strip() # 오후 강수 확률
    
    # 미세먼지
    dust = soup.find("ul", attrs={"class":"today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text() # 미세먼지
    pm25 = dust.find_all("li")[1].get_text() # 초미세먼지
    
    
    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print(pm10.strip())
    print(pm25.strip())
    print()
    
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100"
    create_soup(url)
    
    news_list = soup.find("li", attrs={"class":"sh_item _cluster_content"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    
    news_list = soup.find("li", attrs={"class":"sh_item _cluster_content"}).find_all("li", limit=3) # 3개까지만 가져옴
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a태그의 정보를 사용
        
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = url + a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, index 기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, index 기준 0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    # scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    # scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어 회화 가져오기