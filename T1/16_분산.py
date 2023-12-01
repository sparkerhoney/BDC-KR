# 주어진 데이터 셋에서 f2가 0값인 데이터를 age를 기준으로 오름차순 정렬하고 앞에서 부터 20개의 데이터를 추출한 후,
# f1 결측치(최소값)를 채우기 전과 후의 분산 차이를 계산하시오. (소수점 둘째 자리까지)

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic1.csv')

df = df[df['f2'] == 0].sort_values('age', ascending = True).head(20)


# print('결측치 채우기 전 :', df['f1'].var())
# df['f1'] = df['f1'].fillna(df['f1'].min())
# print('결측치 채우기 전 :', df['f1'].var())

var_f1 = df['f1'].var()
var_f2 = df['f1'].fillna(df['f1'].min()).var()

# print(var_f1)
# print(var_f2)

print(abs(round(var_f2 - var_f1, 2)))
