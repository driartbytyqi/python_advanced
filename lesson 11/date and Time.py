import datetime


currentDate = datetime.datetime.now()



print("year:", currentDate.year)
print("month:", currentDate.month)
print("day:", currentDate.day)
print("hour:", currentDate.hour)
print("minute:", currentDate.minute)
print("second:", currentDate.second)
print("microsecond:", currentDate.microsecond)

print("-------------------------------------------------")

currentDate2 = datetime.datetime.now().date()


print("year:", currentDate.year)
print("month:", currentDate.month)
print("day:", currentDate.day)

timeObject = datetime.time(12,30,45,12345)


print("ora:", currentDate.hour)
print("minute:", currentDate.minute)
print("second:", currentDate.second)
print("microsecond:", currentDate.microsecond)


specific_datetime = datetime.datetime(2024,1,1,12,25,1,2235)

formatdate = specific_datetime.strftime('%d-%m-%y')

print(formatdate)


utc_time = datetime.datetime.now(datetime.timezone.utc)

print("current time:",utc_time)


costum = datetime.timedelta(hours=3)