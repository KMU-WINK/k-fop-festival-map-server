from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import re
from guest.models import AuthUser
from guest.models import TimeStampedModel

class Region(models.Model):
    host = models.ForeignKey(AuthUser, verbose_name="주최 집단", on_delete=models.CASCADE, null=False)
    code = models.CharField(max_length=50, null=False, unique=True, verbose_name="구역 코드")
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name="위도")
    long = models.DecimalField(max_digits=9, decimal_places=6, null=False, verbose_name="경도")


class BoothCategory(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="부스 분류")
    # 첨부파일 추가


class Booth(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=50, null=False, unique=True, verbose_name="부스 코드")
    category = models.ForeignKey(BoothCategory, null=True, on_delete=models.SET_NULL, verbose_name="부스 카테고리")
    name = models.CharField(max_length=100, null=False, verbose_name="부스 이름")
    description = models.TextField(null=True, blank=True, verbose_name="부스 상세설명")
    open_at = models.DateTimeField(null=True, blank=True, verbose_name="오픈 시간")
    close_at = models.DateTimeField(null=True, blank=True, verbose_name="마감 시간")
    is_open = models.BooleanField(default=True, verbose_name="운영 여부")
    waiting = models.CharField(max_length=50, null=False, unique=True, verbose_name="운영 시간")
    phone = PhoneNumberField(blank=True, null=True, verbose_name="부스 문의 번호")

    # HashTag
    hash_tag = models.CharField(max_length=100, null=True, blank=True, verbose_name="해쉬태그")
    tag_set = models.ManyToManyField('HashTag', blank=True)

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.hash_tag)  # hash_tag 에서 해쉬태그 추출

        if not tags:
            return

        for t in tags:
            tag, tag_created = HashTag.objects.get_or_create(name=t)  # 신규 태그 instance 생성
            self.tag_set.add(tag)  # ManyToManyField 에 인스턴스 추가 및 본인 tag_set 에 등록
    # 첨부파일 추가

    
class Review(models.Model, TimeStampedModel):
    stamp_id = models.CharField(max_length=10, null=False, unique=True, verbose_name="스탬프 uuid")
    rating = models.PositiveIntegerField(verbose_name="평점")
    review = models.TextField(verbose_name="평가")

    
class Like(models.Model):
    owner = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True)
    code = models.ForeignKey(Booth, verbose_name="부스 코드", on_delete=models.CASCADE, null=False)

    
class Notice(models.Model, TimeStampedModel):
    name = models.CharField(max_length=100, null=False, verbose_name="공지 제목")
    description = models.TextField(null = False, blank=False, verbose_name="공지 내용")
    onclick_target = models.ForeignKey(Booth, on_delete=models.SET_NULL, null=True)
    phone = PhoneNumberField(blank=True, null=True, verbose_name="학생회 번호")

    
class HashTag(models.Model):
    # booth = models.ForeignKey(Booth, verbose_name="해쉬 태그", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, verbose_name="해쉬태그 이름")

    def __str__(self):
        return self.name

class Stamp(models.Model, TimeStampedModel):
    owner = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True)
    code = models.ForeignKey(Booth, verbose_name="부스 코드", on_delete=models.CASCADE, null=False)
