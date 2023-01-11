from dataclasses import field
from rest_framework import serializers
from .models import CatSearch, DogSearch

# json/xml 형식을 지정함


class CatSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatSearch
        #{breed: 페르시안, 코코: asdf}
        fields = '__all__'
        # { {{breed: 페르시안}, {코코: asdf}}, {breed}
        # fields = ('id', 'name')


class DogSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogSearch
        fields = '__all__'
