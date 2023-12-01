# 주어진 데이터에서 2022년 5월 주말과 평일의 sales컬럼 평균값 차이를 구하시오 (소수점 둘째자리까지 출력, 반올림)

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic2.csv', parse_dates = ['Date'])

# df.info()

# df['Date'] = pd.to_datetime(df['Date'])

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['dayofweek'] = df['Date'].dt.dayofweek

# print(df.head())

df['weekend'] = df['dayofweek'].apply(lambda x: x>= 5)
# print(df.head())

weekend_cond = (df['year'] == 2022) & (df['month'] == 5) & (df['weekend'])
weekday_cond = (df['year'] == 2022) & (df['month'] == 5) & (~df['weekend'])

weekend = df[weekend_cond]['Sales'].mean()
weekday = df[weekday_cond]['Sales'].mean()

print(round(weekend - weekday, 1))