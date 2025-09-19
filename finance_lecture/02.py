#install 경우 아나콘다 터미널에서 진행
# import numpy as np
# data = [1, 2, 3]
# arr = np.array(data)
# print(arr)
# print(type(arr))

# #1. for문 사용
# data = [1, 2, 3]

# result = []
# for i in data:
#     result.append(i*10)
#     print('for result:', result)
# print('final result:', result)

import numpy as np
# arr = np.array([1, 2, 3])
# result = arr * 10
# print(result)
# 자동 코딩 해주는 거 np 자꾸 노로 만드네

#2. 2차원 배열

# import numpy as np 
# data2d = [
#     [1,2,3],
#     [4,5,6], 
#     [7,8,9]
# ]

# #print(data2d[0])

# arr = np.array(data2d)
# print(arr[0 ,  :])  #0번째 행 : 전체
# print(arr[:, 0])      # :전체 행 0번쨰 열

# print(arr.shape)

# 인덱스 슬라이싱 전가지 놓짐. 
# 시험문제 1. 행렬 문제
# 시험문제 2. 슬라이싱 콜롬을 넣어 실제 배열에서 어디부터 어디까지 잘라오는지 

# # 시험문제 2 ) arr[1:2] = a arr[1] = b 
# 과연 a+1 b+1 은 성립이 될까? 
# 안 된다. 

arr = np.arange(20).reshape(4,5)
# print(arr)
# # print(arr[:3])

# result = []
# for row in arr:
#     row_01 = [row[0],row[1]]
#     print('row_01:', row_01)
#     result.append(row_01)
#     print('result:', result)
# print(result)

#이거 위에 이해 필요

# print(arr[:2,:2]) 콜론에 대해 잘 이해하세요
# print(arr[1:4, 2:5]) 어떻게 결과에 도출하게 되는지 열심히 이해해보세요.
# 내가 원하는 범위 도출하기 위해 잘 사용하지만, 헷갈리기에 print로 확인하는 습관을 들여라.

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print('a=', a)
# print('b=', b)

# print('a+b=', a+b)
# print('a*b=', a*b)
# print('a%b=', a%b)  
# 이 브로드캐스팅은 주식에서 종가와 시가의 차이를 구할 때 많이 사용됨.


# print('a+10=', a+10)
#조건 1. 뒤축(열)의 길이가 같다.  조건2. 비교하는 어느 한 축의 길이가 1이다. 그냥 외워주세용!

# high = [92700,92400,92100,94300,92300]
# low = [90000,91100,91700,92100,90900]

# arr_high = np.array(high)
# arr_low = np.array(low)

# arr_diff = arr_high - arr_low
# print('arr_diff=', arr_diff)

# arr_high_x3 = arr_high * 3
# arr_low_x2 = arr_low * 2

# print('arr_high_x3 - arr_low_x2=', arr_high_x3 - arr_low_x2)


# data = [
#     [92700, 92400, 92100, 94300, 92300],
#     [90000, 91100, 91700, 92100, 90900]
# ]
# arr = np.array(data)

# print(arr[0] * 3 + arr[1]  * 2)

# weight = np.array([3, 2]).reshape(2, 1)
# print(weight * arr).sum(axis=0)
#axis: 0이면 x축, 1이면 y축

#최소한의 타자를 쳐서 개발을 하는 게 좋다. 
#어떻게 간단하게 할 수 있을까를 고민하면 실력이 는다. 

# arr = np.array( [10, 20, 30] )
# print(arr > 10)

# arr = np.array([10, 20, 30])
# cond = [False, True, True] #f f t면 30 출력, 요론식~
# print(arr[ cond ])

# arr = np.array([10, 20, 30])
# cond0 = arr > 10
# cond1 = arr < 30
# print(arr[ cond0 & cond1 ])

# &연산은 2개 다 참일 경우만 결과 출력

# arr = np.array([10, 20, 30])
# arr = np.where( arr > 10, 1, 0)
# print(arr)
# arr >10 ,1 0 10보다 크면 1, 아니면 0

# arr = np.array([10, 20, 30])
# arr = np.where( arr > 10, arr+10, arr-10)
# print(arr)
# arr >10 ,arr+10 arr-10 10보다 크면 10더하고 아니면 10빼라

# arr = np.arange(8).reshape(4, 2)
# print('arr=', arr)

# print(arr.sum(axis=0)) #행으로 그룹 합계
# print(arr.sum(axis=1)) #열로 그룹 합계
#헷갈리니 많이 사용해보길

# np.random.randint(46, size = (2,5)) # 2행 5열, 46미만 난수 생성
# print(np.random.randint(46, size = (2,5)))

a = np.arange(4)
print('a=', a)
b = np.arange(4, 8)
print('b=', b)
c = np.vstack([a, b])
print('np.vstack([a, b])=', c)  #수직으로 쌓기 2행 4열
print('np.hstack[a, b]=', np.hstack([a, b])) #수평으로 쌓기 1행 8열


from pandas import Series