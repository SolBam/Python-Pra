"""
def isbn_check(isbn):
    s = 0
    
    for i in range(len(isbn) - 1):
        if (i + 1) % 2 == 1:
            s = s + int(isbn[i]) * 1
        else:
            s = s + int(isbn[i]) * 3
    print("ISBN 1 ~ 12자리의 가중치 반영 합계 : %d" %s)
    
    t = s % 10
    chk = (10 - t) % 10
    print("ISBN 1 ~ 12자리의 체크 기호 값 : %d" %chk)
    
    if chk == int(isbn[12]):
        rst = 1
    else:
        rst = 0
    return rst

isbn = input("ISBN 13자리(-제외) : ")
if len(isbn) == 13:
    rst = isbn_check(isbn)
    if rst == 1:
        print("ISBN 코드 : %s는 검증되었습니다." %isbn)
    else:
        print("ISBN 코드 : %s는 검증되지 않았습니다." %isbn)
else:
    print("ISBN 코드 입력은 -를 제외하고 13자리를 입력해주세요.")
"""
"""
jn = input("주민등록번호 : ")
print(jn[0:2], jn[2:4], jn[4:6])
print(jn[7])
print(jn[-1], jn[-3], jn[-5])
"""