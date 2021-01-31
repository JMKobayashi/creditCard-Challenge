from django.db import models

class CreditCard(models.Model):
    exp_date = models.DateField()
    holder = models.CharField(max_length=30)
    number = models.IntegerField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.holder