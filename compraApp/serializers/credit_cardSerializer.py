from compraApp.models.credit_card import Credit_card
from rest_framework import serializers

class Credit_cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit_card
        fields = ['id','card_name', 'card_number', 'card_franchise', 'bank_name', 'id_user']
