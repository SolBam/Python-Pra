import turtle as t # 터틀 모듈

robot_fn = "robotic_vacuum.gif" # 로봇 청소기 이미지 변수 값으로 설정
rx = [] # 터틀 스크린에서 마우스 클릭이 이루어진 x 좌표를 저장하기 위한 리스트 선언
ry = [] # 터틀 스크린에서 마우스 클릭이 이루어진 y 좌표를 저장하기 위한 리스트 선언
move_cnt = 0 # 터틀 스크린에서 마우스 클릭이 이루어진 횟수 초기화

def move_robot(action): # 매개변수 action의 값에 따라 저장된 지점에 대해 순서대로 이동
    t.clear() # 이전에 표시한 터틀 흔적을 모두 지움
    if action == 0: # action이 0이면 move_cnt-1 까지 반복하면서 이동
        for i in range(move_cnt):
            t.goto(rx[i], ry[i])
    elif action == 1: # action이 1이면 move_cnt-1 부터 0까지 반복하면서 이동
        for i in range(move_cnt-1, -1, -1):
            t.goto(rx[i], ry[i])
    elif action == 2: # action이 2이면 밑의 좌표로 이동
        t.goto(rx[move_cnt-1], ry[move_cnt-1])
    elif action == 3: # action이 3이면 밑의 좌표로 이동
        t.goto(rx[0], ry[0])
    t.penup() # 터틀 펜 올림
    
def clicked(x, y): # 터틀 스크린에서 마우스 클릭이 이루어진 좌표를 저장하는 함수 선언
    global move_cnt # 전역변수로 선언
    move_cnt += 1 # 값을 1 증가함
    rx.append(x) # rx 리스트에 x 좌표 값을 추가
    ry.append(y) # ry 리스트에 y 좌표 값을 추가
    
def list_clear(): # 저장된 모든 좌표 지점을 지우는 함수 선언
    global move_cnt # 전역변수로 선언
    del rx[1:move_cnt] # 값을 모두 삭제
    del ry[1:move_cnt] # 값을 모두 삭제
    move_cnt = 1 # 변수 값을 설정
    
def key_SP(): # 함수 선언 및 move_robot(0) 함수 호출
    move_robot(0)
def key_BS(): # 함수 선언 및 move_robot(1) 함수 호출
    move_robot(1)
def key_s(): # 함수 선언 및 move_robot(2) 함수 호출
    move_robot(2)
def key_r(): # 함수 선언 및 move_robot(3) 함수 호출
    move_robot(3)
def key_e(): # 함수 선언 및 list_clear() 함수 호출
    list_clear()
    
t.setup(600, 600) # 터틀 스크린 크기 설정
s = t.Screen() # 터틀 스크린 생성
t. hideturtle() # 터틀 숨김

s.addshape(robot_fn) # 이미지를 터틀 모양으로 등록
t.shape(robot_fn) # 이미지로 터틀 모양 변경
t.speed(6) # 터틀의 속도 설정
t.penup() # 터틀 펜 올림
clicked(-265, 265) # 터틀의 초기 위치를 등록
t.goto(-265, 265) # 터틀의 초기 위치로 이동
t.showturtle() # 터틀을 나타냄

s.onkey(key_SP, "space") # 터틀 스크린에서 스페이스 키가 눌러지면 함수 호출
s.onkey(key_BS, "BackSpace") # 터틀 스크린에서 백스페이스 키가 눌러지면 함수 호출
s.onkey(key_s, "s") # 터틀 스크린에서 s키가 눌러지면 함수 호출
s.onkey(key_r, "r") # 터틀 스크린에서 r키가 눌러지면 함수 호출
s.onkey(key_e, "e") # 터틀 스크린에서 e키가 눌러지면 함수 호출
s.onscreenclick(clicked) # 터틀 스크린에서 마우스클릭이 이루어지면 함수 호출
s.listen() # 터틀 스크린에서의 이벤트 확인