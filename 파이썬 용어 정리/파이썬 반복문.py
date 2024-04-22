"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end = "")
    print("")
"""
"""
num = int(input("밑변, 높이 :"))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end = "")
    print("")
"""
"""
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end = "")
    for k in range(1, i + 1):
        print("*", end = "")
    print("")
"""
"""
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end = "")
    for k in range(1, i + 1):
        print("*", end = "")
    for l in range(1, i):
        print("*", end = "")
    print("")
"""
"""
s = int(input("시작 :"))
h = int(input("높이 :"))
for i in range(1, h + 1):
    for j in range(1, i + 1):
        s = (s + j - 1) % 10
        print(s, end = "")
        s = s - (j - 1)
    print("")
"""
"""
s = int(input("시작 :"))
h = int(input("높이 :"))
for i in range(1, h + 1):
    for j in range(1, h + 1 - i):
        print(" ", end = "")
    for k in range(1, i + 1):
        s = (s + k - 1) % 10
        print(s, end = " ")
        s = s - (k - 1)
    print(" ")
"""
"""
s = int(input("시작: "))
h = int(input("높이: "))

for i in range(h):
    a = i + 1
    for k in range(1, h+1-i):
        print(" ", end='')
    for j in range(a):
        print((s + j )%10, end=' ')
    print(" ")
"""
"""
s = int(input("시작 :"))
h = int(input("높이 :"))
for i in range(1, h + 1):
    for j in range(1, h + 1 - i):
        print(" ", end = "")
    for k in range(1, i + 1):
        print(s, end = " ")
    s = (s + 1) % 10
    print(" ")
"""
"""
n = 1
num = 2
while True:
    print(n, "번 접으면", 2**n, "mm")
    if num >= 100000:
        break
    n += 1
    num = 2**n
print("횟수 :", n, "두께 :", num)
"""