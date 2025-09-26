# from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510, 7.36],
#     ["036360", "3SOFT", 1790, 1.65],
#     ["005670", "ACTS", 1185, 1.28]
# ]

# columns = ["종목코드", "종목명", "현재가", "등락률"]
# df = DataFrame(data=data, columns=columns) #data 파라미터 = data로 지정해줘야 미래가 편해요
# print(df)

# from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510, 7.36],
#     ["036360", "3SOFT", 1790, 1.65],
#     ["005670", "ACTS", 1185, 1.28]
# ]

# columns = ["종목코드", "종목명", "현재가", "등락률"]
# df = DataFrame(data=data, columns=columns)
# df = df.set_index("종목코드")
# print(df)

# from pandas import DataFrame

# data = [
#     ["037730", "3R", 1510, 7.36],
#     ["036360", "3SOFT", 1790, 1.65],
#     ["005670", "ACTS", 1185, 1.28]
# ]

# columns = ["종목코드", "종목명", "현재가", "등락률"]
# df = DataFrame(data=data, columns=columns)
# df.set_index("종목코드", inplace=True) #inplace=True : 원본을 직접 수정 원본을 지키고 싶으면 False
# print(df)

# from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)
# df.index.name = "종목코드"
# print(df) #index.name : index의 이름을 지정해줌 

# 1번째 그냥 하기
# 2번째 set_index() 사용하기
# 3번째 set_index() 사용하기 with inplace=True (원본 데이터 변경)
# 4번째 index name 속성 사용 

# dataframe 이란? series가 합쳐진 형태 따라서 하나의 행들이 다 series

# from pandas import DataFrame

# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]

# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
# df = DataFrame(data=data, index=index, columns=columns)
# print(df['현재가']) #인덱스로 종목코드를 설정했기에 종목코드도 같이 나옴. 만약 인덱스 설정을 안 하면? 0 1 2로 나옴
# print(df.현재가) #이렇게도 가능

# list = ["현재가", "등락률"]
# print(df[list])

# print(df[['현재가', '등락률']]) #이렇게 3개로 프린트 가능


# s = df['현재가']
# print(s.index)
# print(s.values)

# 데이터 인덱싱을 할 때, 대부분은 시리즈 객체지만! 대괄호 2개 사용하면 데이터프레임

#다시 한 번 기억해야 할 iloc, loc << 
# print(df.iloc[0])
# print(df.iloc[-1])

#iloc 잘 이해하기
#손코딩 해보기. 도움이 됩니다. 
#시험 보기 전 코넬노트애 이쁘게 요약해두기 단권화, 요약
# 키워드쪽에 키워드 적고, 내용 쪽에 내용 적고, 요약 칸에 요약 적기

# 습관을 들이자. 책상에 1시간 앉아 있기 등 

from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

print(df.iloc[0])
print(df.loc['037730'])


########### 시험 문제 
# 행번호로 행 선택 후 시리즈 인덱싱 
# print(df.iloc[0].iloc[1])            # 시리즈 행번호
# print(df.iloc[0].loc["현재가"])        # 시리즈 인덱스 
# print(df.iloc[0]["현재가"])            # 시리즈 인덱스

# # 인덱스로 행 선택 후 시리즈 인덱싱 
# print(df.loc["037730"].iloc[1])      # 시리즈 행번호
# print(df.loc["037730"].loc["현재가"])  # 시리즈 인덱스 
# print(df.loc["037730"]["현재가"])      # 시리즈 인덱스

# iloc으로 하는 게 더 편하지만, 나중에 이해하기 쉽게 만들어야 함. iloc으로 할 거면 주석으로 0이 뭔지를 나타내야 함. 

# 특정 범위 가져오기 p. 111
from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

# print(df.loc[["037730", "036360"]])
# print(df.iloc[[0, 1]]) # 괄호가 2개면 데이터프레임 형태, 0대신 인덱스를 넣어도 된다.

# print(df.loc[["037730", "036360"], ["종목명", "현재가"]]) # sksms dlrj wha dltkdgka gka rhcuhqkdi gkf emkek
print(df.iloc[[0, 1], [0, 1]])