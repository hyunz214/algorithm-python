# -*- coding: utf-8 -*-

a = "Hello"
b = "World"
print(a + " " + b)


# 사전 자료형
a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

# 사전 자료형의 또 다른 초기화 방법
b = {
    '홍길동' : 97,
    '이순신' : 98
}

print(b)
# 특정 키 값 출력
print(b['이순신'])

key_list = b.keys()
print(key_list)


# 집합 자료형
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)
# 교집합
print(a & b)
# 차집합
print(a - b)