import datetime

x = datetime.datetime.now()
print(x)

y = datetime.date(2021, 2, 14)
print(y)

t = datetime.time(16, 39, 4)
print(t)

#출제의도: 라이브러리를 사용할 줄 아는가

m = int(input())
d = int(input())
def findDay(a, b):
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    print(datetime.date(2021, a, b).weekday())
    return day[datetime.date(2021, a, b).weekday()]
print(findDay(m, d))