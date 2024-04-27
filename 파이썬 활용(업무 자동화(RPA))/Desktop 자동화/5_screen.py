import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 28,99 250,250,250 #FAFAFA

pixel = pyautogui.pixel(28, 99)
print(pixel)

# print(pyautogui.pixelMatchesColor(28, 99, (250, 250, 250)))
# print(pyautogui.pixelMatchesColor(28, 99, pixel))
print(pyautogui.pixelMatchesColor(28, 99, (250, 250, 222)))