# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-18 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
            ],
        ),
        migrations.CreateModel(
            name='Url_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='分页链接')),
            ],
        ),
        migrations.CreateModel(
            name='Urls_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.CharField(max_length=100, verbose_name='舞蹈链接')),
                ('ci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo_apps1.City_info')),
            ],
        ),
        migrations.CreateModel(
            name='Users_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leixing', models.CharField(max_length=200, null=True, verbose_name='类型')),
                ('weizhi', models.CharField(max_length=200, null=True, verbose_name='位置')),
                ('lianxi', models.CharField(max_length=200, null=True, verbose_name='联系')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='手机号')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='标题')),
                ('xq', models.TextField(null=True, verbose_name='详情')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo_apps1.Urls_info')),
            ],
        ),
    ]