# -*- coding: utf-8 -*-
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 여덟번째 원소만 출력 
print(a[7])

# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네번째 원소 값 변경 
a[3] = 7
print(a)

# 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 리스트 컴프리헨션
array = [i for i in range(10)]
print(array)

# 조건문도 혼용 가능(홀수만 출력)
array = [i for i in range(10) if i % 2 == 1]
print(array)

# 수들의 제곱 값을 포함하는 리스트 
array = [i * i for i in range(10)]
print(array)

# N X M 크기의 2차원 리스트 초기화 
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array) 