from django.shortcuts import render, redirect
import calendar
import locale
import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Appoinment,OffDays
from user.models import Address,User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from photoshoot.models import Photo_Concept,Shoot_Plan,Shoot_Concept,Concept



def get_days_for_next_four_months():
    #locale.setlocale(locale.LC_ALL, 'turkish') # Add this to setting so that it will be easier to change locale

    obj = calendar.Calendar()
    last_week = []
    days = []
    current_day = datetime.date.today()
    month = datetime.date.today().month
    year = datetime.date.today().year
    lastmonth = month+3
    weektodelete=0
    first = True

    if (month > 9):
        lastmonth = 12
        next_year_month = month - 9
        for x in range(month,lastmonth+1):
            current_li = list(obj.monthdatescalendar(year, x))
            if current_li[0] == last_week:
                current_li.pop(0)
            for x in range(len(current_li)):
                if current_li[x][6] < current_day:
                    weektodelete = weektodelete + 1

            if first:
                for i in range(weektodelete):
                    current_li.pop(0)
            days.append(current_li)
            last_week = current_li[-1]
            first = False

        for x in range(1,next_year_month+1):
            current_li = list(obj.monthdatescalendar(year+1, x))
            if current_li[0] == last_week:
                current_li.pop(0)
            for x in range(len(current_li)):
                if current_li[x][6] < current_day:
                    weektodelete = weektodelete + 1

            if first:
                for i in range(weektodelete):
                    current_li.pop(0)
            days.append(current_li)
            last_week = current_li[-1]
            first = False

    else:
        for x in range(month,lastmonth+1):
            current_li = list(obj.monthdatescalendar(year, x))
            if current_li[0] == last_week:
                current_li.pop(0)
            for x in range(len(current_li)):
                if current_li[x][6] < current_day:
                    weektodelete = weektodelete + 1

            if first:
                for i in range(weektodelete):
                    current_li.pop(0)
            days.append(current_li)
            last_week = current_li[-1]
            first = False
    return days




def combine_off_and_app_days(days,response):
    if response.user.is_admin:
        appoinments = Appoinment.objects.filter(date__range = (days[0][0][0],days[-1][-1][-1]))
    else:
        appoinments = Appoinment.objects.filter(date__range = (days[0][0][0],days[-1][-1][-1]),status = "APR")

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

@login_required
def appoinment_data(response):
    days = get_days_for_next_four_months()
    days_dict,has_appoinment = combine_off_and_app_days(days,response)

    return JsonResponse({'data':list(days),'week':days_dict,'has_app':has_appoinment})

@login_required
def get_week_data(response):
    days = get_days_for_next_four_months()
    days_dict,has_appoinment = combine_off_and_app_days(days,response)

    return JsonResponse({'week':days_dict,'has_app':has_appoinment})


@login_required
def appoinment(response):
    current_user = response.user
    item = Shoot_Plan.objects.filter(user_id=current_user)
    if not item.exists():
        return redirect('/photoshoot/concepts/')

    concept_shoot_items = Shoot_Concept.objects.filter(shoot_id=item[0]).count()
    num_concept = item[0].num_of_concept.number_of_selection
    if not item.exists() or concept_shoot_items != num_concept:
        return redirect('/photoshoot/concepts/')
    return render(response, "appoinment/appoinment.html")

@login_required
def admin_edit(response):
    return render(response, "appoinment/admin_editing.html")

@login_required
def add_or_delete_appoinment(response):
    #ToDo Check is date valid
    app_add = response.POST.get('app_add') #If false it means we are doing deletion
    app_date = response.POST.get('app_date')
    app_time = response.POST.get('app_time')

    if app_add == "true": 
        current_user = response.user
        item = Appoinment.objects.filter(date = app_date, time=app_time)
        if not item.exists():
            appoinment_new_item = Appoinment(user = current_user, date = app_date, time=app_time)
            appoinment_new_item.save()
            return JsonResponse({"result": "success"}, status=200)

    elif response.user.is_admin:
        item = Appoinment.objects.filter(date = app_date, time=app_time)
        if item.exists():
            item[0].delete()
            return JsonResponse({"result": "success"}, status=200)

    else:
        item = Appoinment.objects.filter(date = app_date, time=app_time,user = response.user)
        if item.exists():
            if response.user == item[0].user:
                item.delete()
                return JsonResponse({"result": "success"}, status=200)
        
    return JsonResponse({"result": "fail"}, status=400)

@login_required
def add_or_delete_offday(response):
    if response.user.is_admin:
        off_add = response.POST.get('off_add')#If false it means we are doing deletion
        off_date = response.POST.get('off_date')
        off_time = response.POST.get('off_time')

        if off_add == "true":
            offday_new_item = OffDays(date = off_date, time=off_time)
            offday_new_item.save()
            return JsonResponse({"result": "success"}, status=200)

        else : 
            item = OffDays.objects.filter(date = off_date, time=off_time)
            if item.exists():
                item.delete()
                return JsonResponse({"result": "success"}, status=200)
    return JsonResponse({"result": "fail"}, status=400)

@login_required
def user_info_for_admin(response):
    days = get_days_for_next_four_months()
    appoinments = Appoinment.objects.filter(date__range = (days[0][0][0],days[-1][-1][-1]))
    apps_dict={}
    for x in appoinments:
        date_of_x = x.date.strftime("%Y-%m-%d")
        if date_of_x in apps_dict.keys():
            apps_dict[date_of_x].append((x.user.first_name +" "+ x.user.last_name))
        else:
            apps_dict[date_of_x] = [(x.user.first_name +" "+ x.user.last_name)]
    

    return JsonResponse({'user_app':apps_dict})

@login_required
def user_app_info(response):
    days = get_days_for_next_four_months()
    current_user = response.user
    user_appoinment = Appoinment.objects.filter(date__range =(days[0][0][0],days[-1][-1][-1]),user = current_user)

    if user_appoinment.exists():
        return JsonResponse({'user_app_date':user_appoinment[0].date.strftime("%Y-%m-%d"),'user_app_time':user_appoinment[0].time,'user_name':user_appoinment[0].user.email})
    else:
        return JsonResponse({'user_app_date':None,'user_app_time':None,'user_name':None})

@login_required
def get_user_for_app(response):
    app_date = response.POST.get('app_date')
    app_time = response.POST.get('app_time')

    user_appoinment = Appoinment.objects.filter(date=app_date,time=app_time)
    app_user = user_appoinment[0].user
    address = Address.objects.filter(user=app_user)
    item = Shoot_Plan.objects.filter(user_id=app_user)
    if item.exists():
        shoot_detail = prepare_shoot_details(item[0],app_user)
    else:
        shoot_detail = {}
        shoot_detail["user_name"] = app_user.first_name + " "+ app_user.last_name
        shoot_detail["user_phone"] = app_user.phone

    if response.user.is_admin and user_appoinment.exists():
        user_address_json = serialize('json', address)
        return JsonResponse({"address":serialize("json",address),"shoot":shoot_detail}, status=200,safe=False)
    else:
        return JsonResponse({"result": "unauthorized"}, status=400)

def prepare_shoot_details(shoot,app_user):
    concept_shoot_items = Shoot_Concept.objects.filter(shoot_id=shoot)

    shoot_dict={}
    shoot_dict["type"] = shoot.shoot_type.name
    shoot_dict["album"] = shoot.album_type.type_of_album
    shoot_dict["num_of_concept"] = shoot.num_of_concept.number_of_selection
    concept_names = ""
    for x in concept_shoot_items:
        if concept_names == "":
            concept_names = x.concept_id.name
        else:
            concept_names = concept_names + " , " + x.concept_id.name

    shoot_dict["concepts"] = concept_names
    shoot_dict["user_name"] = app_user.first_name + " "+ app_user.last_name
    shoot_dict["user_phone"] = app_user.phone
    shoot_dict["total_price"] = shoot.num_of_concept.price + shoot.album_type.price

    return shoot_dict