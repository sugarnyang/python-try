user_input = input()
l = list(user_input.split())
print(l)
l = [int(i) for i in l]
print(l)

for i in range(len(l)-1, -1, -1):
    print(l[i], end=' ')