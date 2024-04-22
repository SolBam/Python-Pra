import turtle as t #터틀 그래픽 모듈

def draw_pos(x, y): #이동하는 과정에서 터틀의 흔적을 표시하는 함수
    t.clear() #이전에 표시한 터틀 흔적을 모두 지움
    t.setpos(x, y) #터틀의 위치를 x,y로 변경
    t.stamp() #터틀의 흔적을 남김
    
    hl = -(t.window_height() / 2) #터틀 스크린 높이/2의 값을 음수로 처리하여 스크린 하단의 y축 위치를 h에 대입
    
    tm = 0 #시간 변수 tm을 0으로 초기화
    while True: #무한 반복
        d = (9.8 * tm**2) / 2 #이동거리를 계산하고 값을 d에 대입
        ny = y -int(d) # 클릭한 y좌표에서 이동거리를 뺀 후 결과를 ny에 대입
        if ny > hl:
            t.goto(x, ny) #터틀의 위치를 x,ny로 이동
            t.stamp() #터틀의 흔적을 남김
            tm = tm + 0.3 #tm의 값을 1 증가
        else:
            break #반복 중단
            
t.setup(500, 600) #터틀 스크린의 크기를 지정
t.shape("circle") #터틀 모양 설정
t.shapesize(0.3, 0.3, 0) #터틀의 가로, 세로, 테두리를 설정
t.penup() # 터틀 펜 올림
s = t.Screen() #터틀 스크린 생성
s.onscreenclick(draw_pos) #터틀 스크린에서 마우스 클릭이 이루어지면 콜백 함수 호출
s.listen() #터틀 스크린에서 이벤트 확인