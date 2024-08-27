import datetime
import jdatetime


def leap(dt1,dt2):

    leap_count = 0
    differece = dt2 -dt1

    for x in range(dt1,dt2+1):
        if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
            leap_count += 1

    print(f"leap years: {leap_count} and number of clock changes betwen given dates {differece * 2}")
        

dt1 = input("please enter date in year-month-day-hour-minute-secnod: ").split('-')
dt2 = input("please enter second date in year-month-day-hour-minute-secnod: ").split('-')


dt1 = list(map(lambda y: int(y),dt1))
dt2 = list(map(lambda y: int(y),dt2))
datetime1 = datetime.datetime(*dt1)
datetime2 = datetime.datetime(*dt2)


differece = datetime2 - datetime1
print('difference in seconds: ',(differece.days * 86400) + (differece.seconds))
print('datetime hijri 1:',jdatetime.date.fromgregorian(day=dt1[2],month=dt1[1],year=dt1[0]))
print('datetime hijri 2:',jdatetime.date.fromgregorian(day=dt2[2],month=dt2[1],year=dt2[0]))

leap(dt1[0],dt2[0])


