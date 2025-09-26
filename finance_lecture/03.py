from pandas import Series

# data = [10, 20, 30]
# s = Series(data)
# print(s)

# s = Series(['samsung', 81000])
# print(s)
#series를 사용하면 다양한 타입의 데이터들을 편하게 변수로 지정할 수 있다.

#data = [1000, 2000, 3000]

#인덱스 사용법
# s = Series(data)
# print(s.index)
# print(s.index.to_list())


# data = [1000, 2000, 3000] 
# s = Series(data)
# s.index = ["메로나", "구구콘", "하겐다즈"]
# print(s)

# #숫자가 데이터고, 메로나 구구콘은 인덱스다.

# #인덱스 파라미터 형식
# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]

# s = Series(data, index)
# print(s)

# s = Series(data, index)
# s = Series(data, index=index)
# s = Series(data=data, index=index)
# s = Series(index=index, data=data)
# #3, 4번이 좋지만 1, 2번도 쓰인다
# price = [42500, 42550, 41800, 42550, 42650]
# date = ["2019-a05-31", "2019-05-30", "2019-05-29", "2019-05-28", "2019-05-27"]
# s = Series(price, date)
# print(s)

# 판다스를 사용할 때 꼭 알아야 할 것
# iloc, loc
# data = [1000, 2000, 3000]
# s = Series(data=data)

# print('s.iloc[0]=', s.iloc[0])
# print('s.iloc[1]=', s.iloc[1])
# print('s.iloc[2]=', s.iloc[2])
# print('s.iloc[-1]=', s.iloc[-1])

# iloc은 행기반으로 가져옴. [-1]은 마지막 행

# print('s.loc[0]=', s.loc[0])
# print('s.loc[1]=', s.loc[1])
# print('s.loc[2]=', s.loc[2])
# # print(s.loc[-1])   # 에러

# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]
# s = Series(data=data, index=index)
 
# print(s.iloc[0])
# print(s.loc['메로나'])

#loc은 -1이 안됨. 인덱스 기반으로 가져옴

# print(s['메로나'])
# print(s[0])
# 이거 이제 안 됨. 쓰지마 과거의 유산이야. 과거는 됐는데, 이제 버전업 되면서 안 될 거고, iloc, loc을 써야 함.
# 72~73p는 과감히 x 버려

# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]
# s = Series(data=data, index=index)

# print(s.iloc[0:2]) #iloc은 행 기반

# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]
# s = Series(data=data, index=index)

# print(s.loc['메로나':'구구콘'])

####################################시험문제
# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]
# s = Series(data=data, index=index)

# indice = [0, 2]
# print('s.iloc[ indice] =', s.iloc[ indice ])
# print('s.iloc[ [0,2]] =', s.iloc[ [0, 1, 2] ]) # 콜론과 콤마 구분 콜론은 범위인데, 콤마는 리스트

# # 리스트여서 대괄호가 2개다. 

# data = [1000, 2000, 3000]
# index = ["메로나", "구구콘", "하겐다즈"]
# s = Series(data=data, index=index)

# indice = ["메로나", "하겐다즈"]
# print('s.loc[indice] = ', s.loc[ indice ])
# print('s.loc[["메로나", "하겐다즈"]] = ', s.loc[ ["메로나", "하겐다즈"] ]) # 불연속적인 데이터도 가능하다. 

data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)

# s.loc['메로나'] = 500          # 값 수정
# print(s)
#이렇게 되면 원본데이터가 바뀜. 원본데이터를 바꾸고 싶지 않다면? 튜플을 사용.

# s.iloc[0] = 500            # iloc 연산 사용
# # s['메로나'] = 500          # [ ] 기호 사용 << 이런 건 죄다 잊어 널 괴롭게 할거야.
# s.loc['비비빅'] = 500          # 값 추가, 자동적으로 인덱스 채워서 추가됨 
# print(s)

# print('s.drop('메로나')= ', s.drop('메로나')) #메로나 삭제

# s = s.drop('메로나') #원본데이터를 바꾸고 싶다면 이렇게 해야 함
# print('s =', s)

########################################################## 시험문제_drop 원본데이터 수정을 방지하기 때문

# 철수 = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
# 영희 = Series([10, 30, 20], index=['SKT', 'KT', 'NAVER'])
# 가족 = 철수 + 영희
# print(가족)

# high = Series([42800, 42700, 42050, 42950, 43000])
# low = Series([42150, 42150, 41300, 42150, 42350])

# diff = high - low
# print(diff)

# date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
# high = Series([42800, 42700, 42050, 42950, 43000], index=date)
# low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
# profit = high / low
# # print(profit) #수익률 계산

# # 누적수익률 계산
# print( 'profit.cumprod = ', profit.cumprod( ) )
# print( 'profit.cumprod.iloc[-1] = ', profit.cumprod( ).iloc[ -1 ] ) #가장 최근 데이터 수익률

# data = {
#     "삼성전자": "전기,전자",
#     "LG전자": "전기,전자",
#     "현대차": "운수장비",
#     "NAVER": "서비스업",
#     "카카오": "서비스업"
# }
# s = Series(data)
# print(s.unique()) #series에서 유일한 값들을 뽑아냄

# print(s.value_counts())

# from pandas import Series
# s = Series(["1,234", "5,678", "9,876"])
# print( int(s) ) # 에러 type int형으로는 convert 할 수 없다. 해결법은 function을 만들어서 적용시키는 것

#################################### 시험문제 85p 위쪽 remove 그거
# def remove_comma(x) :
#     print(x, 'in function')
#     return x

# s = Series(["1,234", "5,678", "9,876"])
# result = s.map(remove_comma)
# print(result)

# from pandas import Series

# def remove_comma(x) :
#     return int(x.replace(",", "")) #replace는 문자열에서 특정 문자를 다른 문자로 바꿔줌, ,를 공백으로 대체 | 타입이 int로 됨.

# s = Series(["1,234", "5,678", "9,876"])
# result = s.map(remove_comma)
# print(result)

# def is_greater_than_5000(x):
#     if x > 5000:
#         return "크다"
#     else:
#         return "작다"

# s = Series([1234, 5678, 9876])
# s = s.map(is_greater_than_5000) #파라미터를 쓰면 오류남 이름 써야함. x쓰면 오류남 
# print(s)

# from pandas import Series

# data = [42500, 42550, 41800, 42550, 42650]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']
# s = Series(data=data, index=index)
# cond = s > 42000
# # print(cond)

# print(s[cond])  #조건에 맞는 데이터만 출력 88p. 

# close = [42500, 42550, 41800, 42550, 42650]
# open = [42600, 42200, 41850, 42550, 42500]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

# open = Series(data=open, index=index)
# close = Series(data=close, index=index)

# cond = close > open
# print(cond)

# print(close[cond]) #종가가 시가보다 높은 날의 종가만 출력

# 위처럼 condition을 하던가 아니면 
# print(close[ close > open ]) #이렇게 해도 됨. 이게 중급 개발자임. or 람다 활용

# close = [42500, 42550, 41800, 42550, 42650]
# open = [42600, 42200, 41850, 42550, 42500]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

# open = Series(data=open, index=index)
# close = Series(data=close, index=index)
# diff = close - open
# print(diff[close > open])

# from pandas import Series

# data = [3.1, 2.0, 10.1, 5.1]
# index = ['000010', '000020', '000030', '000040']
# s = Series(data=data, index=index)
# print(s)

# # 정렬 (오름차순)
# s1 = s.sort_values()
# print('오름 = ',s1)

# # 정렬 (내림차순)
# s2 = s.sort_values(ascending=False)
# print('내림 = ',s2)

data = [3.1, 2.0, 10.1, 3.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
print('순위 = ', s.rank()) #숫자가 작을 수록 1등. 1등 2.5등 4등 요론 노낌

print('이쁜 순위 = ',s.rank(ascending =False, method='min')) #이건 이상해서 담시간에 알려드릴게욤
