# 조건 1: 그림판 실행 및 최대화
# 조건 2: 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력 - 참 잘했어요
# 조건 3: 5초 대기 후 그림판 종료 - 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win", "r") # 단축키 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 띄워져 있다고 가정
if window.isMaximized == False:
    window.maximize() # 최대화
    
# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()
    
# 흰 영역 클릭
pyautogui.click(500, 500, duration=0.5)

# btn_brush = pyautogui.locateOnScreen("btn_brush.png")
# pyautogui.click(btn_brush.right + 200, btn_brush.bottom - 200)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # '저장하지 않음' 선택