# 파일 기본
import os

# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("파이썬 활용(업무 자동화(RPA))") # 파이썬 활용(업무 자동화(RPA))으로 작업 공간 이동
# os.chdir("..") # 부모 폴더로 이동
# os.chdir("../..") # 조부모 폴더로 이동
# os.chdir("c:/") # 주어진 절대 경로로 이동

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\frirg\OneDrive\바탕 화면\파이썬 프로그램\파이썬 활용(업무 자동화(RPA))\Desktop 자동화\my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생성 날짜
# ctime = os.path.getctime("run_btn.png")
# print(ctime)
# # 날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("run_btn.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime("run_btn.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize("run_btn.png")
# print(size) # 바이트 단위로 파일 크기 가져오기

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("Desktop 자동화")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기(하위 폴더 모두 포함)
# result = os.walk(".") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []

# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))
        
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# import fnmatch
# pattern = "*.py" # .py로 끝나는 모든 파일
# result = []

# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
#             result.append(os.path.join(root, name))

# print(result)

# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir(".")) # 현재 위치는 폴더인가?
# print(os.path.isfile(".")) # 현재 위치는 파일인가?

# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))

# 만약에 지정된 경로에 해당하는 파일 / 폴더가 없다면?
# print(os.path.isfile("run_btnn.png"))

# 주어진 경로가 존재하는지?
# if os.path.exists("run_btn.png"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 절대 경로로 지정하면 경로 기준으로 폴더 생성
# os.makedirs("new_folder/a/b/c") # 하위 폴더를 가지는 폴더를 생성

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folder_rename") # 폴더 안이 비었을 때만 삭제 가능

import shutil # shell utilities
# shutil.rmtree("new_folder_rename") # 폴더 안이 비어 있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있으므로 주의!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png", "test_folder") # 원본 파일 경로, 대상 폴더 경로
# # 어떤 파일을 폴더 안에 새로운 파일 이름으로 복사하기
# shutil.copy("run_btn.png", "test_folder/copied_run_btn.png") # 원본 파일 경로, 대상 경로(변경된 파일명)
# shutil.copyfile("run_btn.png", "test_folder/copied_run_btn_2.png") # 원본 파일 경로, 대상 파일 경로
# shutil.copy("run_btn.png", "test_folder/copy.png")
# shutil.copy2("run_btn.png", "test_folder/copy2.png") # 원본 파일 경로, 대상 폴더(파일) 경로

# copy, copyfile: 메타 정보 복사 X
# copy2: 메타 정보 복사 O

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2") # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("test_folder", "test_folder3")

# 폴더 이동
# shutil.move("test_folder", "test_folder3") # test_folder를 test_folder3 밑으로 이동
# shutil.move("test_folder2", "test_folder3")
shutil.move("test_folder", "test_folder_rename") # 폴더명 변경되는 효과