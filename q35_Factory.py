def one(n):
    def two(value):
        return value ** n
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))

#2제곱,3제곱,4제곱 할 수 있는 Factory함수를 만들려고 한다.