#s24022
import calendar
import datetime

dt_now = datetime.datetime.now()

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2024, 6,))
print(dt_now)