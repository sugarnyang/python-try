user_input = int(input())
for i in range(1, 10):
    print('{} X {} = {}'.format(user_input, i, user_input*i))

for i in range(1, 10):
    print(user_input * i, end=' ')