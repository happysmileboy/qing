from django.db import models
from django.conf import settings
from django.urls import reverse
from accounts.models import *
# Create your models here.

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    mentor = models.ForeignKey(Mentor_univ, on_delete=models.CASCADE,)
    phone_number = models.IntegerField(verbose_name='휴대폰 번호')
    price = models.CharField(max_length=20, verbose_name='요금제')
    prequestion = models.TextField(verbose_name='사전 질문지')
    date_joined=models.DateTimeField(verbose_name='생성날짜', auto_now_add=True)
    is_deposit=models.BooleanField(default=False, verbose_name='입금완료')
    is_approval=models.BooleanField(default=False,verbose_name='승인완료')
    is_reserved=models.BooleanField(default=False,verbose_name='예약완료')

    def get_absolute_url(self):
        return reverse('payment:mentoring_reserved', kwargs={
            'pk': self.pk,
        })

    def __str__(self):
        return str(self.pk)