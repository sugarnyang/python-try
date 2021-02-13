user_input = input()
l = list(user_input.split())
l = [int(i) for i in l] #int형으로 변환한다.

if l != sorted(l):
    print('NO')
else:
    print('YES')

#sorted와 sort는 다르다.
#sorted는 리스트 내장함수, 리스트를 만진다.
#sort는 리턴된 값을 정렬해서준다. 리스트를 만지지 않는다.

l = [1,6,2,9,0,7,5,8,3]
print(l.sort()) #None
print(sorted(l)) #[0, 1, 2, 3, 5, 6, 7, 8, 9]
print(l) #[0, 1, 2, 3, 5, 6, 7, 8, 9]