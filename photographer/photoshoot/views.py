from django.shortcuts import render


def photo_shoot(response):
    return render(response, "photoshoot/shootplan.html")