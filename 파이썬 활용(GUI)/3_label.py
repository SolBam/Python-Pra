from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="C:\\Users\\frirg\\OneDrive\\바탕 화면\\파이썬 프로그램\\파이썬 활용(GUI)\\image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    
    # Garbage Collection : 불필요한 메모리 공간 해제
    # photo를 설정했는데 나오지 않는다면 변수를 global로 선언을 한다.
    global photo2
    photo2 = PhotoImage(file="C:\\Users\\frirg\\OneDrive\\바탕 화면\\파이썬 프로그램\\파이썬 활용(GUI)\\image2.png")
    label2.config(image=photo2)
    
btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()