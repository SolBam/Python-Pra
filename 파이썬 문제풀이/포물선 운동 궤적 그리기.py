import turtle as t # 터틀 모듈
import math # 수학 모듈

tm = 0.3 # 시간 간격 변수
ux = 0 # x속도
uy = 0 # y속도
dx = 0 # x이동거리
dy = 0 # y이동거리
g = 9.8 # 중력가속도 변수
velo = 0 # 속도 변수
ang = 0 # 각도 변수

def draw_pos(x, y): #이동하는 과정에서 터틀의 흔적을 표시하는 함수
    velo = t.numinput("입력", "속도 :", 50, 10, 100) # 속도를 입력받음
    ang = math.radians(t.numinput("입력", "각도 :", 45, 0, 360)) # 각도를 입력받음, radians 함수로 입력받은 값을 변환하여 대입
    
    t.clearstamps() # 이전에 표시한 터틀 흔적을 모두 지움
    t.hideturtle() # 터틀을 숨김
    t.setpos(x, y) # 터틀의 위치를 x, y로 변경
    t.showturtle() # 터틀을 나타냄
    t.stamp() # 터틀의 흔적을 남김
    
    hl = -(t.window_height() / 2) # 스크린의 하단에 해당하는 y축 위치를 계산하여 대입
    
    ux = velo * math.cos(ang) # x속도를 계산하여 대입
    uy = velo * math.sin(ang) # y속도를 계산하여 대입
    
    while True:
        uy = uy + (-1 * g) * tm # 중력가속도가 반영된 y속도를 계산하여 대입
        dy = t.ycor() + (uy * tm) - (g * tm**2) / 2 # y이동거리를 계산하여 대입
        dx - t.xcor() + (ux * tm) # x이동거리를 계산하여 대입
        if dy > hl:
            t.goto(dx, dy) # 터틀의 위치를 dx, dy로 이동
            t.stamp() # 터틀의 흔적을 남김
        else:
            break # 반복 중단
        
t.setup(600, 600) # 터틀 스크린 크기 설정
t.shape("circle") # 터틀 모양 설정
t.shapesize(0.3, 0.3, 0) # 터틀의 가로, 세로, 테두리 설정
t.penup() # 터틀 펜을 올림
s = t.Screen() # 터틀 스크린 생성
s.onscreenclick(draw_pos) # 터틀 스크린에서 마우스 클릭이 이루어지면 코백 함수 호출
s.listen() # 터틀 스크린에서 이벤트 확인