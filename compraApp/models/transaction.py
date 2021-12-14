from django.db import models
from .credit_card import Credit_card

class Transaction (models.Model):
    id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField()
    transaction_status = models.CharField ('Status', max_length = 20,
    choices=(
        ('A','Aprobada'),
        ('D','Denegada'),
        ('R','Reversado'),
        ('E','En proceso')
    ))
    transaction_value = models.FloatField (default=0)
    store_name = models.CharField ('Store name', max_length = 40)
    id_credit_card= models.ForeignKey(Credit_card, related_name='Transaction', on_delete=models.CASCADE)
