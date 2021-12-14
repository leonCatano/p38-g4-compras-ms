from django.db import models

class Credit_card (models.Model):
    id = models.AutoField(primary_key=True)
    card_name = models.CharField ('Card Name', max_length = 20)
    card_number = models.IntegerField (default=0)
    card_franchise = models.CharField ('Card Franchise', max_length = 20)
    bank_name = models.CharField ('Bank name', max_length = 40)
    id_user= models.IntegerField()
