# # importing calendar module
# import calendar
# import numpy 
# import datetime
# from calendar import monthrange
 
# obj = calendar.Calendar()

# month = datetime.date.today().month
# year = datetime.date.today().year
# lastmonth = month+10



# if (month > 8):
#     lastmonth = 13
    
# days = []

# for x in range(month,lastmonth):
#     current_li = list(obj.monthdayscalendar(year, x))
#     last_li = list(obj.monthdayscalendar(year, x-1))
    
#     current_size = len(current_li)
#     last_size = len(last_li)
    
#     if current_li[current_size-1][6] == 0:
#         current_li.pop()
#     if last_li[last_size-1][6] == 0:
#         last_li.pop()
#     last_day = last_li[len(last_li)-1][6]
        
#     if current_li[0][0] == 0:
#         for i in range(0,7):
#             if current_li[0][i] !=0:
#                 break
#             current_li[0][i] = last_day+i+1
            
#     print(f"-          {x}. Ay           -")
#     days.append(current_li)
#     for day in current_li:
#         print(day)
    

# from datetime import date, timedelta
# import calendar
# import time
# start_time = time.time()

# sdate = date(2022, 3, 15)   # start date
# edate = date(2022, 9, 15)   # end date

# delta = edate - sdate       # as timedelta

# for i in range(delta.days + 1):
#     day = sdate + timedelta(days=i)
#     print(f"{day} of {calendar.day_name[day.weekday()]}")
#     #print(calendar.day_name[day.weekday()] )
    

# print("--- %s seconds ---" % (time.time() - start_time))
# #--- 0.00477147102355957 seconds ---


import calendar
import locale
import datetime

locale.setlocale(locale.LC_ALL, 'turkish')

obj = calendar.Calendar()
 

last_week = []
days = []
month = datetime.date.today().month
year = datetime.date.today().year
lastmonth = month+4



if (month > 8):
    lastmonth = 13

for x in range(month,lastmonth):
    current_li = list(obj.monthdatescalendar(year, x))
    if current_li[0] == last_week:
        current_li.pop(0)
    for day in current_li:
        print(day[3].strftime("%B"))
        for x in day:
            print(x)
        print()
    days.append(current_li)
    last_week = current_li[-1]

# for x in days:
#     for y in x:
#         for z in y:
#             print(z)
#         print(" ")   {{ x[0].strftime("%B") }}

