"""
def indexa(s):
    print("문자열 길이 : ", len(s))
    print("첫번째 문자 : ", s[0])
    print("두번째 문자 : ", s[1])
    print("마지막 문자 : ", s[-1])

a = input("문자열 : ")
indexa(a)
"""
"""
def indexa(s):
    st = ''
    ss = ''
    for i in s:
        st += i
    print("개별 문자 출력 : ", st)
    ss = s[::-1] #슬라이싱 활용
    print("역순 개별 문자 출력 : ", ss)

a = input("문자열 : ")
indexa(a)
"""
"""
items = {"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}
s = 0
while True:
    ob = input("제품명 : ")
    if ob == "라면":
        s = s + items["라면"]
        print("[%s:%d] > %d" %(ob, items[ob], s)) # 포매팅 활용
    elif ob == "":
        break
"""
"""
from math import sqrt
a = int(input('정수 :'))
print(sqrt(a))
"""
"""
sales = {1:8, 2:6, 3:10, 4:13}
for i in sales:
    print(i, "분기 : ", "#" * sales[i])
"""
items = {"공책":325, "연필":427, "지우개":125, "복사지":510}
a = int(input("파악 재고수 기준 : "))
for i in items:
    if a > items[i]:
        print(i, items[i])