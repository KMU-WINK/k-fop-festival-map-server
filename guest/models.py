from django.db import models
from django.contrib.auth.models import User


class GuestToken(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    token = models.CharField(max_length=32, null=False, verbose_name="토큰")
    ip = models.CharField(max_length=15, null=False, verbose_name="아이피")
    userAgent = models.TextField(verbose_name="유저 에이전트")
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name="위도")
    long = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name="경도")
    is_active = models.BooleanField(default=True, null=False, verbose_name="회원 차단 여부")