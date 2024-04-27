import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)

# 특수 문자
# pyautogui.keyDown("shift") # shift키를 누른 상태
# pyautogui.press("4") # 숫자 4을 입력
# pyautogui.keyUp("shift") # shift키를 뗀다.

# 조합키(Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# pyautogui.hotkey("ctrl", "a")

import pyperclip

# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")

# 자동화 프로그램 종료
# win: ctrl + alt + del
# mac: cmd + shift + option + q