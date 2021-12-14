from django.contrib import admin
from .models.account import Account
from .models.credit_card import Credit_card
from .models.transaction import Transaction

admin.site.register(Account)
admin.site.register(Credit_card)
admin.site.register(Transaction)
