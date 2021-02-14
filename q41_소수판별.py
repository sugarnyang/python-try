user_input = int(input())
ch = True #소수면True 소수가아니면False
for i in range(2, user_input):
    if user_input % i == 0:
        ch = False

if ch == True:
    print('YES')
else:
    print('NO')