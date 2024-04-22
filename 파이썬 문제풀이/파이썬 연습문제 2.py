"""
def fadd(n, m):
    s = n + m
    print(n, "+", m, "=", s)

a = 3
b = 4
fadd(a, b)
"""
"""
def calc_gugudan(dan):
    for i in range(1, 10):
        print(dan, "*", i, "=", dan * i, "")

d = int(input("단 : "))
calc_gugudan(d)
"""
"""
def avg(a, b):
    s = (a + b) / 2
    return s

in1 = int(input("값1 : "))
in2 = int(input("값2 : "))
r = avg(in1, in2)
print("평균 : ", r)
"""
"""
def print19(st, ed):
    for i in range(st, ed + 1):
        print(i, end = " ")
    print("")

s = int(input("시작값 : "))
e = int(input("끝값 : "))
if s < e:
    print19(s, e)
else:
    print("시작값이 끝값보다 작아야 합니다.")
"""
"""
def welcome(name):
    print("환영합니다. ", name, "님")

n = input("이름 : ")
welcome(n)
"""
"""
def dispch(ch, n):
    for i in range(1, n + 1):
        print(ch, end = "")

s = input("문자 : ")
c = int(input("횟수 : "))
dispch(s, c)
"""
"""
def maxnum(m, n):
    if m > n:
        print("큰 수 : ", m)
    else:
        print("큰 수 : ", n)

m = int(input("숫자1 : "))
n = int(input("숫자2 : "))
maxnum(m, n)
"""
"""
def pow_xy(x, y):
    r = x**y
    return r
x = int(input("숫자 : "))
y = int(input("제곱수 : "))
s = x**y
print("3 * ", x, "**", y, "+ 5 = ", 3*s+5)
"""
"""
def one2n_sum1(n):
    s = 0
    if n > 0:
        for i in range(1, n + 1):
            s += i
        print("1 -- ", n, "=", s)
    else:
        print("입력된 수가 1보다 작습니다.")
    return s
s = int(input("자연수 : "))
one2n_sum1(s)
"""
"""
def one2nt_sum(n):
    s = 0
    if n == 1:
        for i in range(1, 11):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 2:
        for i in range(1, 21):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 3:
        for i in range(1, 31):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 4:
        for i in range(1, 41):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 5:
        for i in range(1, 51):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 6:
        for i in range(1, 61):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 7:
        for i in range(1, 71):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 8:
        for i in range(1, 81):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 9:
        for i in range(1, 91):
            s += i
        print("1 -- ", n * 10, "=", s)
    elif n == 10:
        for i in range(1, 101):
            s += i
        print("1 -- ", n * 10, "=", s)
    else:
        print("입력값의 법위를 초과하였습니다.")
    return s

num = int(input("자연수 : "))
one2nt_sum(num)
"""
"""
def one2n_sum2(n):
    s = 0
    if n > 0:
        for i in range(1, n + 1):
            s += i
        print("1 -- ", n, "=", s)
    elif n < 0:
        for i in range(1, n * -1 + 1):
            s += i
        print("1 -- ", n, "=", s * -1)
    else:
        print("입력된 수가 0입니다.")
    return s

num = int(input("정수 : "))
one2n_sum2(num)
"""
"""
def m2n_sum(m, n):
    s = 0
    if m > n:
        for i in range(n, m + 1):
            s += i
        print(m, "--", n, "=", s)
    elif n > m:
        for i in range(m, n + 1):
            s += i
        print(m, "--", n, "=", s)
    return s

num1 = int(input("정수 1 :"))
num2 = int(input("정수2 : "))
m2n_sum(num1, num2)
"""
"""
def pzn(num):
    if num > 0:
        print("양수")
    elif num < 0:
        print("음수")
    elif num == 0:
        print("0")

while True:
    n = int(input("정수 : "))
    pzn(n)
    if n == 0:
        break
"""