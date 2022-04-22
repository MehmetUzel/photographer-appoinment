from django.shortcuts import render
from .forms import ShootPlanForm
from .models import Photo_Concept,Shoot_Plan,Shoot_Concept


def photo_shoot(response):
    current_user = response.user
    if response.method == 'POST':
        form = ShootPlanForm(response.POST)
        if form.is_valid():
            shootplan = form.save(commit=False)
            shootplan.user_id = current_user
            shootplan.save()
            # return redirect("user/userprofile.html")
            return render(response, 'photoshoot/shootplan.html', {'form':form})
        else:
            messages.info(response, f'account does not exist plz sign in')

    form = ShootPlanForm()
    item = Shoot_Plan.objects.filter(user_id=current_user)
    if item.exists():
        form = ShootPlanForm(instance = item[0])

    return render(response, 'photoshoot/shootplan.html', {'form':form})

def concept_photos(response):
    concepts = Photo_Concept.objects.filter(concept_id__is_active=True)
    current_user = response.user
    item = Shoot_Plan.objects.filter(user_id=current_user)
    
    if item.exists():
        num_concept = item[0].num_of_concept.number_of_selection
        return render(response, "photoshoot/concepts.html", {'concept':concepts,'num_concept':num_concept})

    return render(response, "photoshoot/concepts.html", {'concept':concepts})


def toggle_concept(response):
    is_add = response.POST.get('is_add')
    conceptid = response.POST.get('concept_id')
    current_user = response.user

    if is_add == "true": 
        item = Shoot_Plan.objects.filter(user_id=current_user)
        if item.exists():
            shoot_concept_new = Shoot_Concept(shoot_id=item[0].id,concept_id=conceptid)
            shoot_concept_new.save()
            return JsonResponse({"result": "success"}, status=200)
        else:
            return JsonResponse({"result": "fail"}, status=400)

    elif is_add == "false":
        item = Shoot_Plan.objects.filter(user_id=current_user,concept_id=conceptid)
        if item.exist():
            item.delete()
            return JsonResponse({"result": "success"}, status=200)
        else:
            return JsonResponse({"result": "fail"}, status=400)

    else:
            return JsonResponse({"result": "fail"}, status=400)


