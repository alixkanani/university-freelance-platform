from django.db import models
from accounts.models import CustomUser
from clinics.models import Clinic

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    specialty = models.CharField(max_length=100, verbose_name='تخصص')
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, verbose_name='مطب')
    about_me = models.TextField(blank=True, verbose_name='درباره من')

    def __str__(self):
        return f"دکتر {self.user.first_name} {self.user.last_name} - {self.specialty}"
