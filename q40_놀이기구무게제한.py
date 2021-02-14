total = 0
count = 0
limit = int(input())
n = int(input())

for i in range(n):
    friend = int(input())
    total += friend
    if total <= limit:
        count = i+1
print(count)