from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers  import Countryerializer
from .models import Country
from .permissions import IsOwner
from rest_framework.parsers import JSONParser 


class AllDataView(APIView):
    def get(self, request):
        data = Country.objects.all()
        cleaned_data = [i for i in data if request.user.pk == i.owner.pk]
        serializer = Countryerializer(cleaned_data, context={'request': request}, many=True)
        return Response(serializer.data)

class CertainDataView(APIView):
    def get(self, request, pk):
        data = Country.objects.get(pk=pk)
        serializer = Countryerializer(data, context={'request': request}, many=False)
        if request.user.pk == data.owner.pk:
            return Response(serializer.data)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateView(APIView): 
    def post(self, request):
        owner = request.user.pk
        data = request.data
        data["owner"] = owner
        serializer = Countryerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateView(APIView):
    def put(self, request, pk):
        try:
            owner = request.user.id
            user = Country.objects.get(pk=pk)
            updated = JSONParser().parse(request) 
            updated["owner"] = owner
            if request.user.pk == user.owner.id: 
                serializer = Countryerializer(user, data=updated)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
            else:
                raise Country.DoesNotExist
        except Country.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteView(APIView):
    def delete(self, request, pk):
        try:
            data = Country.objects.get(pk=pk)
            if request.user.pk == data.owner.pk:
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise Country.DoesNotExist
        except Country.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)