# city와 f4를 기준으로 f5의 평균값을 구한 다음, 
# f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic1.csv')

df = df.groupby(['city', 'f4'])[['f5']].mean()
# print(df)

# reset_index() : groupby 에서 df 형식으로 변환해주는 함수
# sort_values() : df의 컬럼에서 sorting 해주는 함수
df = df.reset_index().sort_values('f5', ascending = False).head(7)
# print(df)

print(round(df['f5'].sum(), 2))