# 2.1 넘파이 설치


# import numpy as np


# * pip install numpy; anaconda envrionment terminal에서 설치

# 2.1.2 넘파이 기초
# ndarray : n차원 배열 


# data = [1, 2, 3]
# arr = np.array(data)
# print('arr =', arr)
# print('type(arr) =', type(arr))


# 배열 변수를 지정할 땐, array의 약자인 arr로 많이 씀.

# 2.1.3 넘파이 연산
# (비경제적 방법): 반복문 사용


# data = [1, 2, 3]
# result = []
# for i in data:
#     result.append(i * 10)
#     print('result =', result)   

# print('final result =', result)


# append: 리스트 result에 요소를 추가하는 코드 

# (경제적 방법): 넘파이 배열 연산
import numpy as np


# arr = np.array([1, 2, 3])
# result = arr * 10
# print('result =', result)


# 2.1.4 2차원 배열


# data2d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print('data2d[0] =', data2d[2])  #파이썬 슬라이드는 [행][열] 



# (경제적 방법)


# data2d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# arr = np.array(data2d)
# print('arr[0, :] =', arr[:,2])  


# : 콜론은 전체를 의미, 행열 숫자 셀 땐 0부터 시작

import numpy as np

arr = np.array([
    [[1, 2, 3], [4, 5, 6]],       # 첫 번째 층
    [[7, 8, 9], [10, 11, 12]]     # 두 번째 층
])