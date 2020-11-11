from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, phone, password, extra_fields):
        kwargs = extra_fields.copy()
        kwargs['grade'] = int(kwargs['grade'][0])
        user = self.model(
            **kwargs
        )
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password):
        user = self.model(
            phone=phone, password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    password = models.CharField(max_length=256, null=True, blank=True, verbose_name="패스워드")
    host = models.ForeignKey('self', default=None, null=True, blank=True,
                               on_delete=models.CASCADE)
    ip = models.CharField(max_length=15, null=True, verbose_name="아이피")
    userAgent = models.TextField(verbose_name="유저 에이전트", null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, verbose_name="위도")
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True, verbose_name="경도")

    phone = PhoneNumberField(unique=True, null=False, verbose_name="휴대폰 번호")
    is_active = models.BooleanField(verbose_name="활성화", default=False)
    is_admin = models.BooleanField(verbose_name="관리자 계정 여부", default=False)
    is_staff = models.BooleanField(verbose_name="스태프 여부", default=False)
    is_superuser = models.BooleanField(verbose_name="최고 관리자 여부", default=False)
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    PASSWORD_FIELD = 'password'

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name_plural = "회원 정보"