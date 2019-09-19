from pandas import Series

data4 = Series([15,53,24,52,93,30,33,80,90,77],
                index = list('abcdefghij'))

data4 = data4.append(Series({'k':150}))
print(data4)

data4.add(100)
print(data4)

print(data4.max())
print(data4.min())

print(data4.describe())

print('k' in data4.index)

print(50 in data4.values)

for i in data4.values:
    print(i)

#data4의 모든 인덱스 라벨과 값을 출력
for i in data4.items():
    print(i)

for idx, val in data4.items():
    print(idx, val)