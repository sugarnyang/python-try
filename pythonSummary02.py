#for i in range
ll = []
for i in range(10):
    ll.append(i)
print(ll)

#지능형 리스트로 바꾸면
ll = [i for i in range(10)]
print(ll)

#구구단을 해보자
for i in range(2, 10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i, j , i*j))

#구구단도 지능형 리스트로 바꾸면? 리스트 형태로 출력된다.
lll = ['{} X {} = {}'.format(i, j , i*j) for i in range(2, 10) for j in range(1,10)]
print(lll)

#다중인자 리스트 순회
l = [(1,10), (2, 20), (3,30), (4,40)]
for i in l:
    print(i)
print(l[3][1])
for i, j in l:
    print(i, j)

#enumerate 순위, 넘버링 할 때 많이 사용
for i, j in enumerate(range(100,1000,100), 1):
    print(i, j)

#elif
a = 10
if a > 10:
    print('hello world')
elif a < 20:
    print('good job')
else:
    print('else')

#class
class Car():
    maxSpeed = 300
    maxPeople = 5
    def start(self):
        print('출발')
    def stop(self):
        print('정지')
    def __str__(self):
        return 'hello 매직메서드'
    def __init__(self):
        print('인스턴스가 만들어질때마다 출력')

k9 = Car()
print(k9.maxPeople)

class Hybrid(Car):
    battery = 1000
    betteryKM = 300

k3 = Hybrid
print(k3.maxSpeed)
print(type(k3))
print(dir(k3))
print(k9)
k5 = Car()
k7 = Car()

#python builtin function (https://docs.python.org/3/library/functions.html)