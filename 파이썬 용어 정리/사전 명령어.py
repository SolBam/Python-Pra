cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet1 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet1["A-3"])
print(cabinet1["B-100"])

cabinet1["A-3"] = "김종국" # 변경
cabinet1["C-20"] = "조세호" # 추가
print(cabinet1)

del cabinet1["A-3"] # 삭제
print(cabinet1)

print(cabinet1.keys()) # 키 값만 출력

print(cabinet1.values()) # value 값만 출력

print(cabinet1.items()) # 키 값과 value 값 같이 출력

cabinet1.clear()
print(cabinet1) # 초기화