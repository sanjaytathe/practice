# from datetime import datetime
# # dt=datetime(year=2020,month=9,day=30)
# # dt=datetime(2020,9,15)
# dt=datetime(2020,9,15,2,45)
# print(dt)


# from datetime import time
# t=time(hour=3,minute=13,second=59)
# y=time(3,13,59)
# print(t)
# print(y)


from datetime import timedelta,date
td=timedelta(days=10)
d=date.today()
print(d+td)