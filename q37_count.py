l = input().split()
count = 0
#최대값 알고리즘?
for i in range(1, len(l)):
    if l.count(l[i-1]) < l.count(l[i]):
        count = i
print(count)
print(l[count])

# 문제 자체가 입력을 랜덤으로 받는게 아니라 한 사람을 몰아서 받아서.
# 문제 입력 > 원영 원영 은비 은비 은비 은비 채연 채연
