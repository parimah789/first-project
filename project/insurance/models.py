from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام‌خانوادگی')
    father_name = models.CharField(max_length=100, verbose_name='نام‌پدر')
    date_of_birth = models.DateField(verbose_name='تاریخ تولد')
    mobile_no = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex='^\+?1?\d{9,15}$',
                message='شماره موبایل معتبر نمی‌باشد.',
            ),
        ],
        verbose_name='شماره موبایل'
    )
    national_id = models.CharField(max_length=10, verbose_name='کدملی')
    shomare_shenasname = models.CharField(max_length=10, verbose_name='شماره‌شناسنامه')
    mahal_sodor = models.CharField(max_length=30, verbose_name='محل صدور')
    sheba = models.CharField(max_length=50, verbose_name='شماره شبا')
    shomare_personel = models.CharField(max_length=30, verbose_name='شماره‌پرسنلی')
    location_of_service = models.CharField(max_length=50, verbose_name='محل خدمت')
    employment_status = models.CharField(max_length=50, verbose_name='وضعیت استخدامی')


class ClientFamily(models.Model):
    client = models.ForeignKey(Client, related_name='Family')
    name = models.CharField(max_length=200, verbose_name='نام‌و‌نام‌خانوادگی')
    father_name = models.CharField(max_length=50, verbose_name='نام‌پدر')
    shomare_shenasname = models.CharField(max_length=10, verbose_name='شماره شناسنامه')
    national_id = models.CharField(max_length=10, verbose_name='کدملی')
    relation = models.CharField(max_length=50, verbose_name='نسبت')