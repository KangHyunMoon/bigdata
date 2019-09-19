from pandas import Series

data4 = Series([15,53,24,52,93,30,33,80,90,77],
                index = list('abcdefghij'))

print(data4[-3:])

print(data4[-3:-1])

print(data4['c':'f'])

print(data4 > 60)

print(data4[data4>60])

print(data4.index)

print(data4.values)

print(data4.dtype)

print(data4.size)