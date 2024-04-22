python = "Python is Amazing"
print(python.lower()) # 소문자로 바꿈
print(python.upper()) # 대문자로 바꿈
print(python[0].isupper()) # 0번째 문자가 대문자이면 True, 소문자이면 False
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java")) # 인수의 첫 부분을 두 번째 부분으로 변경

index = python.index("n") # 문자열의 제일 처음 나오는 인수가 몇번째인지 알려줌
print(index)
index = python.index("n", index + 1) # 문자열의 인수가 2번째로 나오는 부분을 알려줌
print(index)

print(python.find("n")) # 인수가 제일 처음 나오는 부분을 알려줌
print(python.find("Java")) # 문자열에 없는 단어일 경우 -1로 표시

print(python.count("n")) # 문자열 중 인수의 개수가 몇개인지 알려줌