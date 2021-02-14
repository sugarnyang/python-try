# -*- coding: utf-8 -*-
#bin 함수를 사용하지 않고 10진수를 2진수로 변환해서 주기
a = int(input()) 
b = []
while a:
    b.append(str(a % 2))
    a = int(a / 2)
b.reverse()
print(b)
print(''.join(b))
print(int(''.join(b)))