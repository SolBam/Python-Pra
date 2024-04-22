"""
subject = str(input("과목 : "))
score = int(input("점수 : "))
print("선호 과목 : ", subject,"희망 점수 : ", score)
"""
"""
num = int(input("정수 :"))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
"""
"""
kor = int(input("국어 :"))
eng = int(input("영어 :"))
mat = int(input("수학 :"))
avr = (kor + eng + mat) / 3
total = kor + eng + mat
print("총점 :", total)
print("평균 :", avr)
if avr >= 80:
    print("평가 : 잘함")
elif 70 <= avr <= 79:
    print("평가 : 보통")
else:
    print("평가 : 미흡")
"""
"""
year = int(input("연도 :"))
if year % 4 == 0 and year % 100 != 0:
    print("윤년")
elif year % 100 == 0 and year % 400 == 0:
    print("윤년")
else:
    print("평년")
"""
"""
s = 0
for i in range(1, 21):
    if i % 2 == 1:
        continue
    s = s + i
    print("i :", i, ", s :", s)
    if s > 30:
        break
print("i :", i, ", s :", s)
"""
"""
name = ["홍길동", "임꺽정"]
subject = ["국어", "영어", "수학"]
for i in name:
    for j in subject:
        print(i, j)
"""
"""
for i in range(1, 6):
    for j in range(1, 5):
        print("*", end = "")
    print("")
"""