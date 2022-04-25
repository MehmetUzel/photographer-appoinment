from django.shortcuts import render,get_object_or_404
from .forms import ShootPlanForm
from .models import Photo_Concept,Shoot_Plan,Shoot_Concept,Concept
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required



def photo_shoot(response):
    current_user = response.user
    if response.method == 'POST':
        obj = get_object_or_404(Shoot_Plan, user_id = current_user)
        form = ShootPlanForm(response.POST, instance = obj)
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
    current_user = response.user
    item = Shoot_Plan.objects.filter(user_id=current_user)

    if item.exists():
        concepts = Photo_Concept.objects.filter(concept_id__is_active=True, concept_id__type_id=item[0].shoot_type)
        num_concept = item[0].num_of_concept.number_of_selection
        concept_shoot_items = Shoot_Concept.objects.filter(shoot_id=item[0])
        if concept_shoot_items.exists():
            convert_concepts_to_list(concept_shoot_items)
            return render(response, "photoshoot/concepts.html", {'concept':concepts,'num_concept':num_concept,'selected_concepts':convert_concepts_to_list(concept_shoot_items)})
        return render(response, "photoshoot/concepts.html", {'concept':concepts,'num_concept':num_concept})

    return render(response, "photoshoot/concepts.html")

def convert_concepts_to_list(queryset_obj):
    concepts_list=[]
    for x in queryset_obj:
        concepts_list.append(x.concept_id.id)
    return concepts_list

def toggle_concept(response):
    is_add = response.POST.get('is_add')
    conceptid = response.POST.get('concept_id')
    current_user = response.user

    if is_add == "true": 
        item = Shoot_Plan.objects.filter(user_id=current_user)
        concept_shoot_items = Shoot_Concept.objects.filter(shoot_id=item[0]).count()
        num_concept = item[0].num_of_concept.number_of_selection
        if item.exists() and concept_shoot_items < num_concept:
            shoot_concept_new = Shoot_Concept(shoot_id=item[0],concept_id=Concept.objects.get(id=conceptid))
            shoot_concept_new.save()
            return JsonResponse({"result": "success"}, status=200)

    elif is_add == "false":
        item = Shoot_Plan.objects.filter(user_id=current_user)
        if item.exists():
            shoot_concept_delete = Shoot_Concept.objects.filter(shoot_id=item[0],concept_id=Concept.objects.get(id=conceptid))
            if shoot_concept_delete.exists():
                shoot_concept_delete.delete()
                return JsonResponse({"result": "success"}, status=200)

    return JsonResponse({"result": "fail"}, status=400)


