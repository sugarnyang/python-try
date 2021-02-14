import time
t = time.time()
print(t) #1970.01.01 00:00:00 부터 초로 계산된 숫자
print(int(t//(365*24*3600)+1970))