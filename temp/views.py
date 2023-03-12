from rest_framework.response import Response
from rest_framework import status
from .models import CatSearch, DogSearch
from rest_framework.views import APIView
from .serializers import CatSearchSerializer, DogSearchSerializer
from django.http import HttpResponse
from .Search.searchHandler import search


class CatSearchListAPI(APIView):
    def get(self, request):
        breed = request.GET.get('breed')
        queryset = CatSearch.objects.filter(breed=breed)
        print(queryset)
        serializer = CatSearchSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        data = request.data
        queryset = CatSearch.objects.filter(breed=data['breed']).first()
        print(queryset)
        serializer = CatSearchSerializer(
            queryset, data=request.data, partial=True)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("invalid")


class DogSearchListAPI(APIView):
    def get(self, request):
        breed = request.GET.get('breed')
        queryset = DogSearch.objects.filter(breed=breed)
        print(queryset)
        serializer = DogSearchSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        data = request.data
        queryset = DogSearch.objects.filter(breed=data['breed']).first()
        print(queryset)
        serializer = DogSearchSerializer(
            queryset, data=request.data, partial=True)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("invalid")


def hi(request):
    search()
    return HttpResponse("search start")
