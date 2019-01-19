from django.shortcuts import render

# Create your views here.
from .models import Users_info,City_info,Urls_info
from .serializers import CitySerializer,UserSerializer,UrlsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination #分页
from rest_framework import filters
from django_filters.rest_framework import DateFromToRangeFilter,OrderingFilter
class Page(PageNumberPagination):#分页功能
    page_size = 10
    page_query_param = 'page'
    max_page_size = 10
class CityView(ModelViewSet):#CityView
    pagination_class = Page
    queryset = City_info.objects.all()
    serializer_class = CitySerializer
class UserView(ModelViewSet):#UserView
    pagination_class = Page
    queryset = Users_info.objects.all()
    serializer_class = UserSerializer
class UrlsView(ModelViewSet):#UrlsView
    pagination_class = Page
    queryset = Urls_info.objects.all()
    serializer_class = UrlsSerializer

