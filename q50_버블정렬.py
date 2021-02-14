def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-1): #(pass)
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] #pass
    for i in range(n):
        print(data[i], end = ' ')

n = int(input())
data = list(map(int, input().split()))

bubble(n, data)