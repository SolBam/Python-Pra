# 규칙 1: http:// 부분은 제외 => naver.com
# 규칙 2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!" 로 구성


url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0~5 직전까지 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙 3
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))