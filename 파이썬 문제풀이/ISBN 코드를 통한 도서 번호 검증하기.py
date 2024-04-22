def isbn_check(isbn): # 매개변수 isbn에 값을 전달받아 가중치 및 체크 기호 값을 계산하는 함수
    s = 0
    
    for i in range(len(isbn)-1): # 가중치 값 계산의 중간값을 저장하기 위한 변수 s의 값을 0으로 설정
        if (i+1) % 2 == 1: # ISBN 코드의 0부터 11자리까지 반복
            s = s + int(isbn[i]) * 1 # isbn에 홀수 자리의 가중치 1을 곱하여 변수 s에 값을 더함
        else:
            s = s + int(isbn[i]) * 3 # isbn에 짝수 자리의 가중치 1을 곱하여 변수 s에 값을 더함
    print("ISBN 1~12자리의 가중치 반영 합계 : %d"%s)
    
    t = s % 10 # ISBN의 가중치 반영 합계 출력
    chk = (10 - t) % 10 # 변수 s의 가중치 합을 10으로 나누어 나머지 값을 구함
    print("ISBN 1~12자리의 체크 기호 값 : %d"%chk)
    
    if chk == int(isbn[12]): # ISBN 1~12 자리의 체크 기호 값 출력
        rst = 1 # 체크 기호 값이 같으면 rst의 값을 1로 설정
    else:
        rst = 0 # 체크 기호 값이 다르면 rst의 값을 0으로 설정
    return rst # rst의 값을 함수의 결과로 반환

isbn = input("ISBN 13자리(- 제외) : ") # 13자리의 ISBN코드 문자열을 입력 받음

if len(isbn) == 13:
    rst = isbn_check(isbn) # 함수 호출 및 함수 반환 값을 rst에 대입
    if rst == 1:
        print("ISBN 코드 : %s는 검증되었습니다."%isbn) # isbn 코드가 검증되었음을 출력
    else:
        print("ISBN 코드 : %s는 검증되지 않았습니다."%isbn) # isbn 코드가 검증되지 않았음을 출력
else:
    print("ISBN 코드 입력은 -를 제외하고 13자리를 입력해주세요.") # - 문자를 제외한 13자리의 ISBN 코드를 입력하는 안내문을 출력