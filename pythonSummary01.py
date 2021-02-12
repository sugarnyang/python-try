print(range(10)) # range(0, 10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(range(10))) # <class 'range'>
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(20, 10, -2))) # [20, 18, 16, 14, 12]
print()

s = '   test start stop    '
print(s.upper())
print(s.lower())
print(s.rstrip())
print(s.strip())
s = s.strip()
a = s.split(' ')
print(a)
print('!'.join(a))

t = (100, 200, 300)

d = {'a':'aa', 'b':'bbb'} 
print(d['a'])
print(d.values())
print(d.keys())
print(d.items())
l = list(d.items())
print(l[0])

seoul = {'apple':4000,'orange':20000}
jeju = seoul.copy()
seoul['apple'] = 99999
print(jeju)
print(seoul)

