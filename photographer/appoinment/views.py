from django.shortcuts import render
import calendar
import locale
import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Appoinment,OffDays

def get_days_for_next_four_months():
    locale.setlocale(locale.LC_ALL, 'turkish') # Add this to setting so that it will be easier to change locale
    obj = calendar.Calendar()
    last_week = []
    days = []
    month = datetime.date.today().month
    year = datetime.date.today().year
    lastmonth = month+4

    if (month > 8):
        lastmonth = 13
        #What happens when current month is december and you need to display days from next year ?

    for x in range(month,lastmonth):
        current_li = list(obj.monthdatescalendar(year, x))
        if current_li[0] == last_week:
            current_li.pop(0)
        # for day in current_li:
        #     print(day[3].strftime("%B"))
        #     for x in day:
        #         print(x)
        #     print()
        days.append(current_li)
        last_week = current_li[-1]

    return days

def appoinment(response):
    days = get_days_for_next_four_months()
    data = json.dumps(days,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
    appoinments = Appoinment.objects.filter(date__range = (days[0][0][0],days[-1][-1][-1]))
    offdays = OffDays.objects.filter(date__range = (days[0][0][0],days[-1][-1][-1]))

    return render(response, "appoinment/appoinment.html", {'data':data,'appoinment':appoinments,'offday':offdays})
