print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))

user_input = input()
if ord(user_input) >= 65 and ord(user_input) <= 90:
    print('YES')
else:
    print('NO')

#아스키코드