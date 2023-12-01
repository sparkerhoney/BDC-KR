# 이상치를 찾아라(소수점 나이)
# 주어진 데이터에서 이상치(소수점 나이)를 찾고 올림, 내림, 버림(절사)했을때 3가지 모두 이상치 'age' 평균을 구한 다음 모두 더하여 출력하시오

import pandas as pd
import numpy as np

df = pd.read_csv('../data/basic1.csv')

# print(df.shape)
# print(df.head())
# print(df.isnull().sum())

"""
* **np.floor(x)**: x의 소수점 아래를 버리고 정수로 반환합니다.
* **np.ceil(x)**: x의 소수점 아래를 올려 정수로 반환합니다.
* **np.trunc(x)**: x의 소수점을 버리고 x의 가장 가까운 정수로 반환합니다.

위 코드에서는 `df['age']-np.floor(df['age'])!= 0`을 사용하여 소수점 데이터를 찾습니다.
즉, `df['age']`의 값이 `np.floor(df['age'])`의 값과 같지 않은 데이터를 찾습니다.
이 조건을 만족하는 데이터는 소수점 값을 포함하는 데이터입니다.

다음은 각 함수의 결과를 설명합니다.

* **m_ceil**: 소수점 데이터의 평균값을 올림한 값입니다.
* **m_floor**: 소수점 데이터의 평균값을 내림한 값입니다.
* **m_trunc**: 소수점 데이터의 평균값을 버린 값입니다.

예를 들어, 다음과 같은 데이터가 있다고 가정합니다.

```
age
1.2
2.3
3.4
4.5
5.6
6.7
7.8
8.9
9.10
```

이 데이터에서 소수점 데이터는 다음과 같습니다.

```
age
1.2
2.3
3.4
4.5
5.6
6.7
7.8
8.9
```

이 데이터의 평균값은 5.3입니다.

따라서, `m_ceil`은 5.4, `m_floor`은 5.3, `m_trunc`는 5.0이 됩니다.

위 코드는 이상치가 포함된 데이터의 평균값을 올림, 내림, 버림하여 차이를 비교하는 데 사용할 수 있습니다.
"""

# 소수점 데이터 찾기
decimal_point_df = df[(df['age'] - np.floor(df['age'])) != 0]

# 올림
m_ceil = np.ceil(decimal_point_df['age']).mean()
# 내림
m_floor = np.floor(decimal_point_df['age']).mean()
# 버림
m_trunc = np.trunc(decimal_point_df['age']).mean()

print(m_ceil + m_floor + m_trunc)