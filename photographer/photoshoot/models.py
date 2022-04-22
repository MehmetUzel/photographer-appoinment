from django.db import models
from user.models import User
from appoinment.models import Appoinment

# Create your models here.
class Shoot_Type(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return (self.name)

class Concept_Info(models.Model):
    number_of_selection = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return (str(self.number_of_selection)+" adet konsept ücreti : "+str(self.price))

class Album_Info(models.Model):
    type_of_album = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        if self.type_of_album == "İstemiyorum":
            return ("Albüm "+self.type_of_album)
        return (self.type_of_album+" albüm ücreti : "+str(self.price))

class Concept(models.Model):
    type_id = models.ForeignKey(Shoot_Type, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return (self.type_id.name+" "+self.name +" konsepti")

class Photo_Concept(models.Model):
    concept_id = models.ForeignKey(Concept, on_delete=models.PROTECT)
    file_url = models.ImageField(upload_to= 'images/', max_length=1000)
    def __str__(self):
        return (self.concept_id.name+" konseptinin fotoğrafı")

class Shoot_Plan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    shoot_type = models.ForeignKey(Shoot_Type, on_delete=models.PROTECT)
    album_type = models.ForeignKey(Album_Info, on_delete=models.PROTECT)
    num_of_concept = models.ForeignKey(Concept_Info, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.user_id.first_name+" "+self.user_id.last_name+" adlı kullanıcının çekim planı")

class Shoot_Appoinment(models.Model):
    shoot_id = models.ForeignKey(Shoot_Plan, on_delete=models.PROTECT)
    appoinment_id = models.ForeignKey(Appoinment, on_delete=models.PROTECT)
    def __str__(self):
        return (self.shoot_id.user_id.first_name+" "+self.shoot_id.user_id.last_name+" adlı kullanıcının " + self.appoinment_id.date.strftime("%Y-%m-%d") +" tarihli "+ self.appoinment_id.time+" çekim planı")

class Shoot_Concept(models.Model):
    shoot_id = models.ForeignKey(Shoot_Plan, on_delete=models.PROTECT)
    concept_id = models.ForeignKey(Concept, on_delete=models.PROTECT)
    def __str__(self):
        return (self.shoot_id.user_id.first_name+" "+self.shoot_id.user_id.last_name+" adlı kullanıcının çekim planı "+self.concept_id.name+" konsepti")

class Payment(models.Model):
    EFT = 'EFT'
    CASH = 'CASH'
    PAYMENT_TYPES = [
        (EFT, 'EFT/HAVALE'),
        (CASH, 'Nakit'),
    ]

    shoot_id = models.ForeignKey(Shoot_Plan, on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    payment_choice = models.CharField(max_length=45, choices=PAYMENT_TYPES)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return (self.shoot_id.user_id.first_name+" "+self.shoot_id.user_id.last_name+" adlı kullanıcının çekiminin ödeme durumu")
