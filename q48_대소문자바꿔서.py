s = input()
result = []

for i in s:
    if i.islower():
        result.append(i.upper())
    else:
        result.append(i.lower())

print(''.join(result)) #이게 진짜 자주 쓰이는건지 궁금