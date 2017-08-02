# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=31, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('summray', models.TextField(verbose_name=b'\xe6\x91\x98\xe8\xa6\x81')),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('createdTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('editTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe8\xbf\x91\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('category', models.CharField(max_length=31, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb')),
                ('category_num', models.IntegerField(default=0, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe7\xbc\x96\xe5\x8f\xb7')),
                ('vistedNumber', models.IntegerField(default=0, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe9\x87\x8f')),
                ('keywords', models.CharField(max_length=63, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d')),
            ],
        ),
        migrations.CreateModel(
            name='Mesage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leave_msg', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('createdTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('editTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe8\xbf\x91\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('code', models.CharField(default=b'', max_length=6)),
                ('phone', models.CharField(default=b'', max_length=11)),
            ],
        ),
    ]
