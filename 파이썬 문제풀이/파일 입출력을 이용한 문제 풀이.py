# 조건: 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만든다.
"""
- x 주차 주간 보고 -
부서 :
이름 :
업무 요약 :
"""

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간 보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")