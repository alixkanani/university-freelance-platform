from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام مطب')
    address = models.TextField(verbose_name='آدرس')
    phone_number = models.CharField(max_length=15, verbose_name='شماره تماس')
    working_hours = models.CharField(max_length=100, blank=True, verbose_name='ساعات کاری')

    def __str__(self):
        return self.name
