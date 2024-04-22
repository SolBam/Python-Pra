# 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3: random 모듈의 shuffle 과 sample 을 활용

from random import *
users = range(1, 21) # 1부터 20까지의 숫자 생성
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print("__ 당첨자 발표 __")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print("__ 축하합니다 __")