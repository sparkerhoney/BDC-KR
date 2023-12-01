# 2022년 5월 sales의 중앙값을 구하시오

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic2.csv')

# print(df.head())
# print(df['Sales'].median())

# df.info()

df['Date'] = pd.to_datetime(df['Date'])
# df.info()

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

# print(df.head())

print(df[(df['year'] == 2022) & (df['month'] == 5)]['Sales'].median())