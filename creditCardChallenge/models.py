from django.db import models

class CreditCard(models.Model):
    exp_date = models.CharField(max_length=10,blank=False)
    holder = models.CharField(max_length=30,blank=False)
    number = models.CharField(max_length=16,blank=False)
    cvv = models.CharField(max_length=4,blank=False)
    brand = models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.holder