# -*- coding: utf-8 -*- 
# 문제5 : for문 계산
# - 다음 코드의 출력 값으로 알맞은 것은?
# ```python
# a = 10
# b = 2
# for i in range(1, 5, 2):
#     a += i
#
# print(a+b)
# ```
# 1)  10
# 2)  12
# 3)  14
# 4)  16

# 정답 4.
# for i in range(1, 5, 2) (start, stop, step) 1, 3, 5. 마지막 5는 출력하지 않음
print(list(range(1, 5, 2)))
a = 10
b = 2
for i in range(1, 5, 2):
    a += i
print(a+b)