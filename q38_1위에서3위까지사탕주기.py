l = input().split() # 97 86 75 66 55 97 85 97 97 95
l = [int(i) for i in l] # 전체가 다 int형으로 변환된다.
print(l)

count = 0

for i in range(3):
    top = max(l) #가장 큰 값
    count += l.count(top)
    print('{}등 점수: {}'.format(i+1 , top))
    for j in range(l.count(top)):
        l.remove(top)
print('1등부터 3등까지는 {}명'.format(count))

