import turtle as t # 터틀 모듈

color_status = ["white", "blue", "red"] #리스트를 상태에 해당하는 색상으로 초기화
alert_status = ["정상", "주의", "화재"] # 리스트를 화재경보기 상태에 해당하는 문자열로 초기화
tempc = 50 # 입력받은 현재 온도의 기본 값 대입

def check_fire(): # 온도에 따른 상태를 나타내는 문자열/색상을 표시하는 함수
    if tempc < 80:
        status = 0 # status에 0 대입
    elif tempc < 120:
        status = 1 # status에 1 대입
    else:
        status = 2 # status에 2 대입
    
    t.clear() # 이전에 표시한 터틀 흔적을 모두 지움
    t.home() # 터틀의 위치를 초기 위치로 변경
    t.pendown() # 터틀 펜 내림
    t.fillcolor(color_status[status]) # status의 값에 따라 color_status 리스트의 원 색상 지정
    t.begin_fill() # 원 그리기 준비
    t.circle(20) # 원 크기를 지정
    t.end_fill() # 원 그리기
    t.penup() # 터틀 펜 올림
    t.goto(-22, 50) # 상태, 온도 출력을 위해 이동
    t.write("%s : %d"%(alert_status[status], tempc)) # status의 값에 따라 alert_status 리스트의 문자열과 tempc 온도 출력

def keyUp(): # tempc의 값에 따라 온도를 5도 또는 10도 감소하는 함수 선언
    global tempc # 변수 tempc를 전역 변수로 선언
    if tempc < 80:
        tempc = tempc + 5 # tempc의 값을 5 증가시킴
    else:
        tempc = tempc + 10 # tempc의 값을 10 증가시킴
    check_fire() # 함수 호출
    
def keyDown(): # tempc의 값에 따라 온도를 5도 또는 10도 감소하는 함수 선언
    global tempc # 변수 tempc를 전역 변수로 선언
    if tempc < 80:
        tempc = tempc - 5 # tempc의 값을 5 감소시킴
    else:
        tempc = tempc - 10 # tempc의 값을 10 감소시킴
    check_fire() # 함수 호출
    
t.setup(300, 300) # 터틀 스크린 크기를 설정
s = t.Screen() # 터틀 스크린 생성
t.hideturtle() # 터틀을 숨김
t.speed(0) # 터틀의 속도를 설정
check_fire() # 함수 호출
s.onkey(keyUp, "Up") # 터틀 스크린에서 위 방향키가 눌러지면 함수 호출
s.onkey(keyDown, "Down") # 터틀 스크린에서 아래 방향키가 눌러지면 함수 호출
s.onkey(s.bye, "q") # 터틀 스크린에서 q키가 눌러지면 터틀 스크린 종료
s.listen() # 터틀 스크린에서 이벤트 확인