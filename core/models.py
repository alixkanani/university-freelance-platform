from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    is_read = models.BooleanField(default=False, verbose_name='آیا خوانده شده؟')

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
