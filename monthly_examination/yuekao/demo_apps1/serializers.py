from rest_framework import serializers
from .models import City_info,Url_info,Urls_info,Users_info
class CitySerializer(serializers.ModelSerializer): #CitySerializer
    class Meta:
        model = City_info
        fields ='__all__'
class UserSerializer(serializers.ModelSerializer):#UserSerializer
    class Meta:
        model = Users_info
        fields = '__all__'
class UrlsSerializer(serializers.ModelSerializer):#UrlsSerializer
    class Meta:
        model = Users_info
        fields = '__all__'

