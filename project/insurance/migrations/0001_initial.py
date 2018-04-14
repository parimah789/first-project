# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 10:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام\u200cخانوادگی')),
                ('father_name', models.CharField(max_length=100, verbose_name='نام\u200cپدر')),
                ('date_of_birth', models.DateField(verbose_name='تاریخ تولد')),
                ('mobile_no', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='شماره موبایل معتبر نمی\u200cباشد.', regex='^\\+?1?\\d{9,15}$')], verbose_name='شماره موبایل')),
                ('national_id', models.CharField(max_length=10, verbose_name='کدملی')),
                ('shomare_shenasname', models.CharField(max_length=10, verbose_name='شماره\u200cشناسنامه')),
                ('mahal_sodor', models.CharField(max_length=30, verbose_name='محل صدور')),
                ('sheba', models.CharField(max_length=50, verbose_name='شماره شبا')),
                ('shomare_personel', models.CharField(max_length=30, verbose_name='شماره\u200cپرسنلی')),
                ('location_of_service', models.CharField(max_length=50, verbose_name='محل خدمت')),
                ('employment_status', models.CharField(max_length=50, verbose_name='وضعیت استخدامی')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام\u200cو\u200cنام\u200cخانوادگی')),
                ('father_name', models.CharField(max_length=50, verbose_name='نام\u200cپدر')),
                ('shomare_shenasname', models.CharField(max_length=10, verbose_name='شماره شناسنامه')),
                ('national_id', models.CharField(max_length=10, verbose_name='کدملی')),
                ('relation', models.CharField(max_length=50, verbose_name='نسبت')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Family', to='insurance.Client')),
            ],
        ),
    ]
