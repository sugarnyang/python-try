def f(n):
    return n  ** 2

print(list(map(f, [2,3,4])))


#
a = [1,2,3,4]
b = [100,200,300,400]
c = ['a','b','c','d']

print(list(zip(a, b, c)))