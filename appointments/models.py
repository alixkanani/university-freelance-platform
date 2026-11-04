from django.db import models
from doctors.models import Doctor
from accounts.models import CustomUser

# کلاس Schedule (برنامه زمانی پزشک)
class Schedule(models.Model):
    DAYS_OF_WEEK = (
        ('sat', 'شنبه'), ('sun', 'یکشنبه'), ('mon', 'دوشنبه'),
        ('tue', 'سه‌شنبه'), ('wed', 'چهارشنبه'), ('thu', 'پنجشنبه'), ('fri', 'جمعه'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='پزشک')
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK, verbose_name='روز هفته')
    start_time = models.TimeField(verbose_name='ساعت شروع')
    end_time = models.TimeField(verbose_name='ساعت پایان')
    is_available = models.BooleanField(default=True, verbose_name='آیا فعال است؟')

    def __str__(self):
        return f"{self.doctor} - {self.get_day_of_week_display()}"

# کلاس Appointment (نوبت)
class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'در انتظار'),
        ('confirmed', 'تایید شده'),
        ('canceled', 'لغو شده'),
        ('done', 'انجام شده'),
    )
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='بیمار')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='پزشک')
    appointment_time = models.DateTimeField(verbose_name='زمان نوبت')
    duration = models.IntegerField(default=15, verbose_name='مدت زمان (دقیقه)')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='وضعیت')
    reason = models.TextField(blank=True, verbose_name='دلیل مراجعه')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    PAYMENT_STATUS = (
        ('unpaid', 'پرداخت نشده'),
        ('paid', 'پرداخت شده'),
    )
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='unpaid', verbose_name='وضعیت پرداخت')


    def __str__(self):
        return f"{self.patient.username} - {self.doctor} - {self.appointment_time}"

