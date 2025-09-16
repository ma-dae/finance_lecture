# # 테슬라 주식 데이터 다운로드 및 5% 이상 상승시각화

# import pandas as pd
# import yfinance as yf

# # 테슬라 주식 데이터 다운로드 (최근 3년, 일간 간격) 
# tsla = yf.download('TSLA', period='3y', interval='1d')
# tsla.head()

# # 상승률 계산: (종가 - 시가) / 시가 * 100
# tsla['Daily_Return_%'] = (tsla['Close'] - tsla['Open']) / tsla['Open'] * 100

# # 5% 이상 상승한 날만 보기
# tsla_up_5 = tsla[tsla['Daily_Return_%'] >= 5]
# print(tsla_up_5[['Open', 'Close', 'Daily_Return_%']])

# import matplotlib.pyplot as plt

# plt.figure(figsize=(12,6))
# plt.plot(tsla.index, tsla['Daily_Return_%'], label='Daily Return (%)')
# plt.axhline(5, color='red', linestyle='--', label='5% 기준선')
# plt.legend()
# plt.title('테슬라 일일 상승률')
# plt.ylabel('%')
# plt.grid(True)
# plt.show()

# # 상승을 어떻게 분석하는지 시범삼아 봄. 


import yfinance as yf
import pandas as pd

tickers = ['TSLA', 'NVDA', 'AMD']
raw_data = yf.download(tickers, start="2022-01-01", end="2024-12-31", group_by='ticker')

# 종목별로 풀어서 하나의 DataFrame으로 합치기
dfs = []
for ticker in tickers:
    df = raw_data[ticker].copy()
    df['Ticker'] = ticker  # 종목 정보 추가
    df['Date'] = df.index  # 날짜 정보 추가
    dfs.append(df.reset_index(drop=True))

# 하나의 DataFrame으로 병합
combined_df = pd.concat(dfs, ignore_index=True)

combined_df['price_change_%'] = combined_df.groupby('Ticker')['Close'].pct_change() * 100
combined_df['avg_volume_20'] = combined_df.groupby('Ticker')['Volume'].rolling(window=20).mean().reset_index(level=0, drop=True)
combined_df['volume_spike'] = combined_df['Volume'] / combined_df['avg_volume_20']
combined_df['is_spike'] = ((combined_df['price_change_%'] >= 5) | (combined_df['volume_spike'] >= 300)).astype(int)

#예측용 라벨 생성 (급등 전조 탐지)
combined_df['target'] = combined_df['is_spike'].shift(-1)  # 다음날 급등 여부
combined_df['volume_ratio'] = combined_df['Volume'] / combined_df['avg_volume_20']
combined_df = combined_df.dropna(subset=['avg_volume_20', 'target'])  # 결측값 제거

X = combined_df[['price_change_%', 'volume_ratio']]
y = combined_df['target']

#학습용 테스트용 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

#모델 학습
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

#모델 평가
from sklearn.metrics import classification_report
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

#실시간 예측
today = combined_df.iloc[-1][['price_change_%', 'volume_ratio']].values.reshape(1, -1)
prediction = model.predict(today)
print("내일 급등 예측:", prediction[0])

# 시각화
import matplotlib.pyplot as plt

for ticker in tickers:
    df_plot = combined_df[combined_df['Ticker'] == ticker]
    plt.figure(figsize=(12, 6))
    plt.plot(df_plot['Date'], df_plot['price_change_%'], label='Daily Rise Rate(%)')
    plt.scatter(
        df_plot[df_plot['is_spike'] == 1]['Date'],
        df_plot[df_plot['is_spike'] == 1]['price_change_%'],
        color='red', label='JUMP MODEL', marker='o'
    )
    plt.axhline(5, color='orange', linestyle='--', label='5% baseline')
    plt.title(f'{ticker} JUMP MODEL detection outcome')
    plt.xlabel('Date')
    plt.ylabel('Rise rate(%)')
    plt.legend()
    plt.grid(True)
    plt.show()

# 결과 요약
print(combined_df[combined_df['is_spike'] == 1][['Date', 'Ticker', 'price_change_%', 'volume_spike']])

# for ticker in tickers:
#     df = yf.download(ticker, period='1y', interval='1d')
#     df = df.reset_index()  # 인덱스 초기화
#     df['Volume'] = df['Volume'].squeeze()  # 2차원 → 1차원 변환
#     df['price_change_%'] = (df['Close'] - df['Open']) / df['Open'] * 100
#     df['avg_volume_20'] = df['Volume'].rolling(window=20, min_periods=20).mean().fillna(0)
#     df['volume_spike'] = (df['Volume'] / df['avg_volume_20']) * 100  # iloc[:, 0] 삭제!
#     df['is_spike'] = (
#         (df['price_change_%'] >= 5) |
#         (df['volume_spike'] >= 300)
#     ).astype(int)
#     df['ticker'] = ticker
#     labeled_data.append(df)


# combined_df = pd.concat(labeled_data, ignore_index=True)  # 인덱스 무시하고 합치기

# 이후 코드 동일
# combined_df['target'] = combined_df['is_spike'].shift(-1)
# combined_df['volume_ratio'] = combined_df['Volume'] / combined_df['avg_volume_20']
# # combined_df = combined_df.dropna(subset=['avg_volume_20', 'target'])

# X = combined_df[['price_change_%', 'volume_ratio']]
# y = combined_df['target']


# # 예측용 라벨 생성 (급등 전조 탐지)
# df['target'] = df['is_spike'].shift(-1)
# df['volume_ratio'] = df['Volume'].iloc[:, 0] / df['avg_volume_20']
# df = df.dropna(subset=['avg_volume_20', 'target'])

# # # 모델 학습
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split

# X = df[['price_change_%', 'volume_ratio']]
# y = df['target']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# model = RandomForestClassifier()
# model.fit(X_train, y_train)


# # 모델 평가
# from sklearn.metrics import classification_report

# y_pred = model.predict(X_test)
# print(classification_report(y_test, y_pred))


# #실시간 판단용 로직
# today = df.iloc[-1][['price_change_%', 'volume_ratio']].values.reshape(1, -1)
# prediction = model.predict(today)
# print("내일 급등 예측:", prediction[0])