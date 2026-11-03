from django.contrib.auth.models import AbstractUser
from django.db import models


# کلاس پایه User (طبق نمودار)
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'مدیر سیستم'),
        ('doctor', 'پزشک'),
        ('secretary', 'منشی'),
        ('patient', 'بیمار'),
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='شماره همراه')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient', verbose_name='نقش')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # رفع خطای تداخل با مدل پیش‌فرض جنگو
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# کلاس Patient (ارث‌بری از User)
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    national_id = models.CharField(max_length=10, unique=True, verbose_name='کد ملی')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد')
    gender = models.CharField(max_length=10, blank=True, verbose_name='جنسیت')

    def __str__(self):
        return f"بیمار: {self.user.first_name} {self.user.last_name}"


# کلاس Secretary (منشی - ارث‌بری از User)
# نکته: این کلاس به Clinic وصل میشه که در اپ clinics تعریف میشه
class Secretary(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.SET_NULL, null=True, verbose_name='مطب')

    def __str__(self):
        return f"منشی: {self.user.first_name} {self.user.last_name}"
