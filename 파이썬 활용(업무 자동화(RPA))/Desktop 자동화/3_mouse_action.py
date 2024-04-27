import pyautogui

# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(20, 57, duration=1) # 1초동안 (20, 57)좌표로 이동 후 마우스 클릭
# pyautogui.click() # mouseDown, mouseUp을 합쳐서 click을 실행한다고 생각하면 된다.
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(500, 500)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(700, 800)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

pyautogui.sleep(3)
# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1214, 83)
# pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100만큼, y 0만큼 드래그
# pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 값 설정
# pyautogui.dragTo(1514, 83, duration=0.25) # 절대 좌표 기준으로 x 1514, y 83로 드래그

pyautogui.scroll(300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤