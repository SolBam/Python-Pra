# import travel.thailand # 패키지로 만든 폴더 안에 있으면 안됨
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import * # __init__ 파일에서 '__all__' 을 활용해서 출력을 만들 수 있다.
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect # 모듈 위치 확인 하는 함수
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))