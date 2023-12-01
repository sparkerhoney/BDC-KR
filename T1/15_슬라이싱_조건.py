# 주어진 데이터 셋에서 age컬럼 상위 20개의 데이터를 구한 다음 f1의 결측치를 중앙값으로 채운다.
# 그리고 f4가 ISFJ와 f5가 20 이상인 f1의 평균값을 출력하시오.

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic1.csv')
df = df.sort_values('age', ascending = False)

# print(df.head(20))

df = df.head(20)
df['f1'] = df['f1'].fillna(df['f1'].median())

# print(df)

# cond = (df['f4'] == 'ISFJ') & (df['f5'] >= 20)

# print(df[cond]['f1'].mean())

print(df[(df['f4'] == 'ISFJ') & (df['f5'] >= 20)]['f1'].mean())