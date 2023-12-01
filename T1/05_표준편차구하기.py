# 조건에 맞는 데이터 표준편차 구하기
# 주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic1.csv')

# print(df['f4'])
# print(df[df['f4']=='ENFJ'])
enfj = df[df['f4']=='ENFJ']['f1'].std()
# print(enfj)

infp = df[df['f4']=='INFP']['f1'].std()
# print(infp)

# np.abs : 절댓값 구하는 Numpy 함수
print(np.abs(enfj - infp))