from django.shortcuts import render
import calendar
import locale
import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Appoinment,OffDays
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required


def get_days_for_next_four_months():
    #locale.setlocale(locale.LC_ALL, 'turkish') # Add this to setting so that it will be easier to change locale
    #To Do ** Start displaying from current week and disable adding entries from past.

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
        days.append(current_li)
        last_week = current_li[-1]

    return days


def combine_off_and_app_days(days,response):
    
    appoinments = Appoinment.objects.filter(date__range = (days[0][0][0],days[-1][-1][-1]))
    offdays = OffDays.objects.filter(date__range = (days[0][0][0],days[-1][-1][-1]))
    current_user = response.user
    user_appoinment = Appoinment.objects.filter(date__range =(days[0][0][0],days[-1][-1][-1]),user = current_user)

    if user_appoinment.exists():
        has_appoinment = True
    else:
        has_appoinment = False

    days_dict = {}
    days_dict = add_appoinments_offdays(days_dict, appoinments)
    days_dict = add_appoinments_offdays(days_dict, offdays)

    return days_dict, has_appoinment


def add_appoinments_offdays(days_dict, app_off):
    for x in app_off:
        date_of_x = x.date.strftime("%Y-%m-%d")
        if date_of_x in days_dict.keys():
            days_dict[date_of_x].append(x.time)
        else:
            days_dict[date_of_x] = [x.time]
    return days_dict

def appoinment_data(response):
    days = get_days_for_next_four_months()
    days_dict,has_appoinment = combine_off_and_app_days(days,response)

    return JsonResponse({'data':list(days),'week':days_dict,'has_app':has_appoinment})


def get_week_data(response):
    days = get_days_for_next_four_months()
    days_dict,has_appoinment = combine_off_and_app_days(days,response)

    return JsonResponse({'week':days_dict,'has_app':has_appoinment})


@login_required
def appoinment(response):
    return render(response, "appoinment/appoinment.html")

@login_required
def admin_edit(response):
    return render(response, "appoinment/admin_editing.html")

#add deletion to method name
@login_required
def add_appoinment(response):
    #ToDo Check is date valid
    app_add = response.POST.get('app_add') #If false it means we are doing deletion
    app_date = response.POST.get('app_date')
    app_time = response.POST.get('app_time')

    if app_add == "true": 
        print("hell")
        current_user = response.user

        appoinment_new_item = Appoinment(user = current_user, date = app_date, time=app_time)
        appoinment_new_item.save()

        return JsonResponse({"result": "success"}, status=200)

    elif response.user.is_admin:
        print("heaven")
        item = Appoinment.objects.filter(date = app_date, time=app_time)
        if item.exists():
            item.delete()
            return JsonResponse({"result": "success"}, status=200)
        
    #search for django error results
    return JsonResponse({"result": "success"}, status=400)

#add deletion to method name
@login_required
def add_offday(response):
    #ToDo *** Admin user required
    if response.user.is_admin:
        off_add = response.POST.get('off_add')#If false it means we are doing deletion
        off_date = response.POST.get('off_date')
        off_time = response.POST.get('off_time')

        if off_add == "true":
            offday_new_item = OffDays(date = off_date, time=off_time)
            offday_new_item.save()
            print("yes problem")
            return JsonResponse({"result": "success"}, status=200)

        else : 
            item = OffDays.objects.filter(date = off_date, time=off_time)
            if item.exists():
                item.delete()
                return JsonResponse({"result": "success"}, status=200)
    #search for django error results
    return JsonResponse({"result": "success"}, status=400)
