from django.db import models
from authentication.models import User

# Create your models here.
class Contracts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    company_details = models.CharField(max_length=100)
    date_contract_started = models.IntegerField()

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
