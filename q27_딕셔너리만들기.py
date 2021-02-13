key = input().split(' ')
value = map(int, input().split(' '))

result = dict(zip(key, value))
print(result)