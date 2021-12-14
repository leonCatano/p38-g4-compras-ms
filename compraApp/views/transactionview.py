from rest_framework.response import Response
from django.conf import settings
from django.db import reset_queries
from django.db.models.query import QuerySet
from rest_framework import request, status, views, generics
from rest_framework.serializers import Serializer
from rest_framework import generics
from compraApp.serializers.credit_cardSerializer import Credit_cardSerializer
from compraApp.serializers.transactionSerializer import TransactionSerializer
from compraApp.models.transaction import Transaction
from compraApp.models.credit_card import Credit_card


#ESTE ES EL CRUD DEL PROYECTO
#Retorna un listado con filtro

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self, *args, **kwargs):
        querySet = Transaction.objects.filter(id_credit_card__id_user=self.kwargs['user'])
        return querySet

#Retorna un solo registro
class TransactionDetailView(generics.RetrieveAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args,**kwargs)

#Crear una transacción
class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def post(self, request, *args, **kwargs):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Transaction Success", status=status.HTTP_201_CREATED)

#Elimina una transacción
class TransactionDeleteView(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        queryset = Transaction.objects.filter(id = kwargs['pk']).filter(id_credit_card__id_user=self.kwargs['user']).first()

        if str(queryset) == "None":
            return Response("Not found",status=status.HTTP_404_NOT_FOUND)

        queryset.delete()
        return Response("Successful transaction delete", status=status.HTTP_200_OK)

#Actualiza una transacción
class TransactionUpdateView(generics.UpdateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def put(self, request, *args, **kwargs):
        return super().update(request, *args,**kwargs)
