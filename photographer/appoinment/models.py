from django.db import models
from user.models import User
# Create your models here.

class Appoinment(models.Model):
    MORNING = 'MO'
    NOON = 'NO'
    EVENING = 'EV'
    TIMES = [
        (MORNING, 'Morning'),
        (NOON, 'Noon'),
        (EVENING, 'Evening'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=30, choices=TIMES)
    creation_date = models.DateTimeField(auto_now=True)


class OffDays(models.Model):
    MORNING = 'MO'
    NOON = 'NO'
    EVENING = 'EV'
    ALLDAY = 'ALL'
    TIMES = [
        (MORNING, 'Morning'),
        (NOON, 'Noon'),
        (EVENING, 'Evening'),
        (ALLDAY, 'AllDay'),
    ]

    date = models.DateField()
    time = models.CharField(max_length=30, choices=TIMES)
