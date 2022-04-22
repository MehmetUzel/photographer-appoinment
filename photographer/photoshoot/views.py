from django.shortcuts import render
from .forms import ShootPlanForm
from .models import Photo_Concept


def photo_shoot(response):
    form = ShootPlanForm()
    return render(response, "photoshoot/shootplan.html",{'form':form})

def concept_photos(response):
    concepts = Photo_Concept.objects.all()
    return render(response, "photoshoot/concepts.html", {'concept':concepts})