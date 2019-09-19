# Pandas 라이브러리 임포트
import pandas
import pandas as pd #as를 통해 별칭 부여
from pandas import Series

#data1 = pandas.Series([3,5,1,2])
#data1 = pd.Series([3,5,1,2])
data1 = Series([3,5,1,2])

print(data1)

print(type(data1.values))
#pandas는 numpy기반으로 구현되어 있음

#값은 모든 데이터 타입이 가능함
data2 = Series(['big data', 30,5000, 40.5])

print(data2)

#인덱스 라벨 추가
data2.index = ['강의명','수강생', '가격', '비고']

print(data2)

print(data2['강의명'])

#숫자 인덱스로도 색인가능
print(data2[2])

#사전 타입으로도 series 가능
data3 = Series({'A':50, 'B':30, 'C':20})
print(data3)


data4 = Series([15,53,24,52,93,30,33,80,90,77],
                index = list('abcdefghij'))
print(data4)

#특정 인덱스로 접근(숫자 인덱스)
#5번째 항목 출력
print(data4[4])

#인덱스 라벨로 접근
#인덱스 라벨이 'f'인 항목을 출력
print(data4['f'])

#여러 인덱스 접근
#숫자 인덱스가 2,4,6인 항목을 출력
print(data4[[2,4,6]])
#외부 괄호: 색인하겠다
#내부 괄호: list를 의미

#인덱스 라벨이 'b','d','h' 인 항목 출력
print(data4[['b','d','h']])

#역인덱스
#가장 마지막 항목 출력
#data4[9]
#data4[data4.size-1] #타 언어의 경우
print(data4[-1])

print(data4[-3])
#마지막에서 3번째

