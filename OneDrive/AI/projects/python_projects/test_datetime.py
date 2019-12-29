import datetime as dt
import time

#get today's date
today_dt = dt.date.today()
print(today_dt)

#get today's date and time
today_timestamp_dt = dt.datetime.now(tz=None).strftime("%Y-%m-%d %H:%M:%S.%f")
print(type(today_timestamp_dt))
print(today_timestamp_dt)

#extract hour from today's timestamp
today_hour = dt.datetime.strptime(today_timestamp_dt, "%Y-%m-%d %H:%M:%S.%f").strftime("%H")
#today_hour = today_hour.strftime("%H")
print(type(today_hour))
print(today_hour)