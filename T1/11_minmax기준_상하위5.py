# min-max스케일링 기준 상하위 5% 구하기
# 주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('../data/basic1.csv')

# print(df.isnull().sum()) # f5에 결측치 없음.
# print(df['f5'])

scaler = MinMaxScaler()

df['f5_1'] = scaler.fit_transform(df[['f5']])

# print(df.head())

lower = np.percentile(df['f5_1'], 5)
upper = np.percentile(df['f5_1'], 95)

print(lower, upper)
print(lower + upper)