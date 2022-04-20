from django.shortcuts import render
from .forms import ShootPlanForm


def photo_shoot(response):
    form = ShootPlanForm()
    return render(response, "photoshoot/shootplan.html",{'form':form})