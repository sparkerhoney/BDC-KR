# 문제 : 이상치를 찾아라.
# 데이터에서 IQR을 활용해 Fare컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오.

import pandas as pd
import numpy as np

"""
IQR은 Interquartile Range의 약자로, 사분위수 범위라고도 합니다.
데이터의 25번째 백분위수(Q1)와 75번째 백분위수(Q3)의 차이로 정의됩니다.
즉, 데이터의 중간 50%가 차지하는 범위입니다.

IQR은 데이터의 산포를 측정하는 데 사용되는 통계량입니다.
표준편차와 비슷한 역할을 하지만, 표준편차는 데이터의 분산을 측정하는 데 더 민감합니다.
IQR은 이상치(outlier)를 식별하는 데에도 사용됩니다.
일반적으로 IQR의 1.5배 이상 떨어진 데이터는 이상치로 간주됩니다.

IQR을 계산하는 방법은 다음과 같습니다.

```
IQR = Q3 - Q1
```

예를 들어, 다음과 같은 데이터가 있다고 가정합니다.

```
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

이 데이터의 25번째 백분위수는 5이고, 75번째 백분위수는 8입니다.
따라서, IQR은 다음과 같이 계산됩니다.

```
IQR = 8 - 5 = 3
```

즉, 이 데이터의 중간 50%는 3의 범위 안에 있습니다.
IQR은 데이터의 산포를 측정하는 데 유용한 통계량입니다. 특히, 이상치를 식별하는 데 효과적입니다.
"""

# 데이터 불러오기
df = pd.read_csv('../data/Titanic.csv')

# 데이터 EDA
# print(df.shape)
# print(df.isnull().sum())
# print(df.head())

# IQR 구하기
Q1 = np.percentile(df['Fare'], 25)
Q3 = np.percentile(df['Fare'], 75)

IQR = Q3 - Q1

## 이상치 기준
# Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

# 이상치 데이터 구하기
outdata1 = df[df['Fare'] < (Q1 - 1.5 * IQR)]
outdata2 = df[df['Fare'] > (Q3 + 1.5 * IQR)]

# print(len(outdata1)) # 0
# print(len(outdata2)) # 116

# 이상치 데이터에서 여성 수 구하기
print(sum(outdata2['Gender'] == 'female'))