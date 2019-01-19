from django.db import models

# Create your models here.
class City_info(models.Model):
    city = models.CharField(max_length=20,verbose_name='城市')
class Url_info(models.Model):
    url = models.CharField(max_length=100,verbose_name='分页链接')
class Urls_info(models.Model):
    urls = models.CharField(max_length=100,verbose_name='舞蹈链接')
    ci = models.ForeignKey(City_info,on_delete=models.CASCADE)
class Users_info(models.Model):
    leixing = models.CharField(max_length=200,null=True,verbose_name='类型')
    weizhi = models.CharField(max_length=200,null=True,verbose_name='位置')
    lianxi = models.CharField(max_length=200,null=True,verbose_name='联系')
    phone = models.CharField(max_length=200,null=True,verbose_name='手机号')
    title = models.CharField(max_length=200,null=True,verbose_name='标题')
    xq = models.TextField(null=True,verbose_name='详情')
    user = models.ForeignKey(Urls_info,on_delete=models.CASCADE)