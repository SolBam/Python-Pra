def comp(seq): #상보적 문자열 변환을 위한 comp() 함수 선언
    comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} #딕셔너리 자료형을 이용하여 값 선언
    seq_comp = "" #변환된 문자들을 연속적으로 누적하여 대입하고자 변수 seq_comp를 빈 문자열로 초기화
    for char in seq: #변수 char에 매개변수 seq의 문자 값을 대입하면서 seq 문자 순으로 반복
        seq_comp = seq_comp + comp_dict[char] #딕셔너리 자료형인 comp_dict는 comp_dict[0]과 같이 숫자 인덱스를 사용하여 값을 얻을 수 없고, comp_dict["A"]와 같이 키를 이용하여 접근해야 함. 해당하는 값을 구한 후 변수 seq_comp에 연속적으로 누적하여 대입
    return seq_comp #변수 seq_comp의 값을 반환

def rev(seq): #역순 문자열 변환을 위한 rev() 함수 선언
    seq_rev = "".join(reversed(seq)) #문자열 반환 함수인 reverse() 함수를 이용하여 매개변수 seq의 문자열을 역순으로 변환하여 반환, 반환된 역순 문자열을 join() 함수를 이용하여 빈 문자열에 결합함
    return seq_rev #변수 seq_rev의 값을 반환

def rev_comp(seq): #상보적 역순 문자열 변환을 위한 rev_comp() 함수 선언
    tmp = comp(seq) #comp() 함수를 이용하여 상보적 문자열로 변환
    return rev(tmp) #rev() 함수를 이용하여 역순 문자열로 변환하여 값을 대입

src = input("DNA sequence : ") #DNA 염기서열 문자열을 입력받아 변수 src에 대입
cnvt = int(input("1(comp), 2(Rev), 3(Rev_Comp): ")) #변환 방식에 해당하는 숫자 1,2,3을 입력받아 변수 cnvt에 대입
if(cnvt >= 1 and cnvt <= 3): #변수 cnvt의 값이 1,2,3일 경우 해당 변환 함수를 호출하여 변환된 결과를 출력하고, 그렇지 않으면 올바른 입력 방법을 안내하는 문자열 출력
    if(cnvt == 1):
        rst = comp(src)
    elif(cnvt == 2):
        rst = rev(src)
    else:
        rst = rev_comp(src)
    print(src, "->", rst)
else:
    print("1(comp), 2(Rev), 3(Rev_Comp)!!")