# 수치형 변수 변환하기
# 주어진 데이터에서 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 그 중앙값을 구하시오

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../data/basic1.csv')

scaler = StandardScaler()
df['f5'] = scaler.fit_transform(df[['f5']])
# print(df.head())

print(df['f5'].median())