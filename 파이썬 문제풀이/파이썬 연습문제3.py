"""
def fc(temper, action):
    if action == 0:
        tmp = temper * 1.8 + 32
        print("C2F : ", temper, "=>", tmp)
    elif action == 1:
        tmp = (temper - 32) / 1.8
        print("F2C : ", temper, "=>", tmp)
    return tmp

t = int(input("온도 : "))
a = int(input("변환(0:C2F, 1:F2C) : "))
fc(t, a)
"""
"""
def welcome(name, msg = "환영합니다."):
    print(msg, name, "님")

n = input("이름 : ")
welcome(n)
welcome(n, "반갑습니다.")
"""
"""
def calc(num1, num2, act = "+"):
    if act == "+":
        print(num1 + num2)
    elif act == "*":
        print(num1 * num2)
    elif act == "/":
        print(num1 / num2)
    elif act == "-":
        print(num1 - num2)
    elif act == "^":
        print("잘못된 연산기호입니다.")

n1 = int(input("정수1 : "))
n2 = int(input("정수 2: "))
calc(n1, n2)
calc(n1, n2, "*")
calc(n1, n2, "^")
"""
def vsum(*num):
    s = 0
    a = ''
    for i in num:
        s = s + i
        if len(num) < i:
            a =  i + '+'
        print(a)
    print(i,s)

vsum(2, 3)
vsum(2, 3, 4)
vsum(2, 3, 4, 5)