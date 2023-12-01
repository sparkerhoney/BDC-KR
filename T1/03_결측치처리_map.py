
# 결측치 처리
# 주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고, 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력하세요!

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic1.csv')

# print(df)
# print(df.isnull().sum())
# print(df.shape)

# 결측치 비율 확인
missing_value_df = df.isnull().sum() / df.shape[0]
# print(missing_value_df)

# 결측치 비율이 80% 이상인 컬럼 삭제
# print("삭제 전 : ", df.shape)
df = df.drop(columns = ['f3'])
# print("삭제 후 : ", df.shape)

# 도시 컬럼 확인
# print(df['city'].unique())

# 각 도시 별 중앙값 계산
s = df[df['city'] == '서울']['f1'].median()
k = df[df['city'] == '경기']['f1'].median()
b = df[df['city'] == '부산']['f1'].median()
d = df[df['city'] == '대구']['f1'].median()

# print(s, k, b, d)

print("대체 전 데이터 샘플 : ")
print(df[18:21])

df['f1'] = df['f1'].fillna(df['city'].map({'서울' : s, '경기' : k, '부산' : b, '대구' : d}))
print("대체 후 데이터 샘플 : ")
print(df[18:21])

# 결과 출력
print(df['f1'].mean())
