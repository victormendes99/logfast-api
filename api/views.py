from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .service.search_itens import list_all_itens, search_itens, get_item
from .serializers import itens_serializer

class AllItensList(APIView):
    def get(self, request, format=None):
        itens = list_all_itens()
        serializer = itens_serializer.ItemSerializer(itens, many=True, context = {"request": request})
        return Response(serializer.data)

class SearchItensList(APIView):
    def get(self, request, format=None):
        item = self.request.query_params.get('item', None)
        preventiva = self.request.query_params.get('preventiva', None)
        itens = search_itens(item, preventiva)
        serializer = itens_serializer.ItemSerializer(itens, many=True, context = {"request": request})
        return Response(serializer.data)

class getItem(APIView):
    def get(self, request, format=None):
        item = self.request.query_params.get('item', None)
        item = get_item(item)
        serializer = itens_serializer.ItemSerializer(item, context = {"request": request})
        return Response(serializer.data)