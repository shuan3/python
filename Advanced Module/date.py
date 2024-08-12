import datetime

mytime = datetime.time()
print(mytime)


today = datetime.date.today()
print(today)
print(today.day)
print(today.ctime())

today = datetime.date.today()
print(today)
print("ctime:", today.ctime())
print("tuple:", today.timetuple())
print("ordinal:", today.toordinal())
print("Year :", today.year)
print("Month:", today.month)
print("Day  :", today.day)

print("Earliest  :", datetime.date.min)
print("Latest    :", datetime.date.max)
print("Resolution:", datetime.date.resolution)

from datetime import datetime

print(datetime(2021, 10, 3, 15, 20, 1))


d1 = datetime.date(2015, 3, 11)
print("d1:", d1)

d2 = d1.replace(year=1990)
print("d2:", d2)


d1 - d2
