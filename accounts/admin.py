from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Patient, Secretary

class CustomUserAdmin(UserAdmin):
    # اضافه کردن فیلدهای ما به پنل ادمین
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات تکمیلی', {'fields': ('phone_number', 'role')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Secretary)
