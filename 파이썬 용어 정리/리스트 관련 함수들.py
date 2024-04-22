subway = ["유재석", "조세호", "박명수"]
print(subway)

subway.append("하하") # 리스트에 추가(끝 쪽에 추가됨)
print(subway)

subway.insert(1, "정형돈") # 처음 인수는 추가할 자리, 2번째 인수는 추가할 것
print(subway)

print(subway.pop()) # 리스트 끝부터 한개씩 뺀다.
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 리스트에 같은 이름이 몇 개인지 확인

num_list = [5,2,4,3,1]
num_list.sort() # 리스트 정렬하기
print(num_list)

num_list.reverse() # 리스트를 역순으로 정렬
print(num_list)

num_list.clear() # 리스트에 들어있는 것을 모두 지움
print(num_list)

mix_list = ["조세호", 20, True] # 다양한 자료형 함께 사용
print(mix_list)

mix_list = ["조세호", 20, True]
num_list = [5,2,4,3,1]
num_list.extend(mix_list) # 리스트 확장
print(num_list)