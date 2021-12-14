
from django.utils import translation
from compraApp.models.transaction import Transaction
from compraApp.models.credit_card import Credit_card
from compraApp.serializers.credit_cardSerializer import Credit_cardSerializer
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id','transaction_date', 'transaction_status', 'transaction_value', 'store_name','id_credit_card']

    def to_representation(self, obj):
        transaction = Transaction.objects.get(id=obj.id)
        credit_card_id=transaction.id_credit_card
        credit_card = Credit_card.objects.get(id=credit_card_id.id)
        return{
                    'id': transaction.id,
                    'transaction_date': transaction.transaction_date,
                    'transaction_status': transaction.transaction_status,
                    'transaction_value': transaction.transaction_value,
                    'store_name': transaction.store_name,
                    'credit_card': {
                        'id': credit_card.id,
                        'card_name': credit_card.card_name,
                        'card_number': credit_card.card_number,
                        'card_franchise': credit_card.card_franchise,
                        'bank_name':credit_card.bank_name,
                        'id_user': credit_card.id_user
                    }
                    }
