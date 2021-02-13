data = input()
word = input()
print (data.find(word))

print(dir('hello world abc'))
print('hello world abc'.find('world'))
print('hello world abc'.find('?')) #없을경우 -1 반환
print('hello world abc'.index('world'))
# print('hello world abc'.index('?')) #에러