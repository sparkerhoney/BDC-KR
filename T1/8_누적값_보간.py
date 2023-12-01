# 주어진 데이터 셋에서 'f2' 컬럼이 1인 조건에 해당하는 데이터의 'f1'컬럼 누적합을 계산한다.
# 이때 발생하는 누적합 결측치는 바로 뒤의 값을 채우고, 누적합의 평균값을 출력한다.
# (단, 결측치 바로 뒤의 값이 없으면 다음에 나오는 값을 채워넣는다)

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic1.csv')
# print(df['f1'][15:22])

# 'f2' 컬럼이 1인 조건에 해당하는 데이터의 'f1'컬럼 누적합을 계산
df2 = df[df['f2']==1]['f1'].cumsum()
# print(df2)

# 누적합 결측치를 바로 뒤의 값으로 채우기
df2 = df2.fillna(method = 'bfill')
# print(df2)

# 누적합의 평균 출력
print(df2.mean())