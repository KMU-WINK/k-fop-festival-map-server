from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Region(models.Model):
    host = models.ForeignKey(User, verbose_name="주최 집단", on_delete=models.CASCADE)
    code = models.CharField(max_length=50, null=False, unique=True, verbose_name="구역 코드")
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name="위도")
    long = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name="경도")


class BoothCategory(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="부스 분류")
    # 첨부파일 추가


class Booth(models.Model):
    host = models.ForeignKey(User, verbose_name="주최 집단", on_delete=models.CASCADE)  # 총학생회 번호
    code = models.CharField(max_length=50, null=False, unique=True, verbose_name="부스 코드")
    category = models.ForeignKey(BoothCategory, null=True, on_delete=models.SET_NULL, verbose_name="부스 카테고리")
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=False, verbose_name="부스 이름")
    description = models.TextField(null=True, blank=True, verbose_name="부스 상세설명")
    open_at = models.DateTimeField(null=True, blank=True, verbose_name="오픈 시간")
    close_at = models.DateTimeField(null=True, blank=True, verbose_name="마감 시간")
    is_open = models.BooleanField(default=True, verbose_name="운영 여부")
    waiting = models.CharField(max_length=50, null=False, unique=True, verbose_name="운영 시간")
    phone = PhoneNumberField(blank=True, null=True, verbose_name="부스 문의 번호")
    # 첨부파일 추가


class Notice(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="공지 제목")
    description = models.TextField(null = False, blank=False, verbose_name="공지 내용")
    onclick_target = models.ForeignKey(Booth, on_delete=models.SET_NULL, null=True)
    phone = PhoneNumberField(blank=True, null=True, verbose_name="학생회 번호")
