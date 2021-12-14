
from rest_framework.response import Response
from django.conf import settings
from django.db import reset_queries
from django.db.models.query import QuerySet
from rest_framework import request, status, views, generics
from rest_framework.serializers import Serializer
from compraApp.models.credit_card import Credit_card
from compraApp.serializers.credit_cardSerializer import Credit_cardSerializer



#Crea la tarjeta para el usuario que hace el request
class CreditCardCreateView(generics.CreateAPIView):
    serializer_class = Credit_cardSerializer

    def post(self, request, *args, **kwargs):
        serializer = Credit_cardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(id_user=self.kwargs ['user'])
        return Response("Successful credit card creation", status=status.HTTP_201_CREATED)

#Enlista las tarjetas de un usuario
class CardListView(generics.ListAPIView):
    serializer_class = Credit_cardSerializer

    def get_queryset(self, *args, **kwargs):
        querySet = Credit_card.objects.filter(id_user=self.kwargs['user'])
        return querySet

#Elimina una tarjeta
class CreditCardDeleteView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        queryset = Credit_card.objects.filter(id = kwargs['pk']).filter(id_user=self.kwargs['user']).first()
        if str(queryset) == "None":
            return Response("Not found",status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response("Successful credit card delete", status=status.HTTP_200_OK)


class CreditCardUpdateView(generics.UpdateAPIView):
    serializer_class = Credit_cardSerializer
    queryset = Credit_card.objects.all()

    def put(self, request, *args, **kwargs):
        return super().update(request, *args,**kwargs)
