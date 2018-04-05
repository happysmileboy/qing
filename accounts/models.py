from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, name=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('The given email must be set')
        if name:
            name = self.normalize_name(name)
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, name=name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', default=False)
        extra_fields.setdefault('is_staff', default=False)
        return self._create_user(username, name ,email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        verbose_name='아이디'
    )
    name = models.CharField(max_length=10, verbose_name='이름',
        unique=False,
        null=True)
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    email = models.EmailField(_('이메일'), blank=True,
        unique=True,)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(verbose_name='active', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    NAME_FIELD= 'name'

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return str(self.name)


class University(models.Model):
    name =models.CharField(max_length=20,verbose_name='대학교')

    def __str__(self):
        return self.name


class Categorized(models.Model):
    name = models.CharField(max_length=20, verbose_name='분류')
    university = models.ForeignKey(University, related_name='categorized', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=30, verbose_name='학부,학과')
    categorized = models.ForeignKey(Categorized, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_mentee = models.BooleanField(default=True)


class Mentor_univ(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d/',
        blank=True,
        null=True,
    )
    phone_number = models.IntegerField(verbose_name='휴대전화')
    univ_categories = models.ForeignKey(Department, verbose_name='학교/계열/학과', related_name='univ_category', on_delete=models.CASCADE)
    consult_kind = models.CharField(max_length=20, verbose_name='상담가능분야')
    detail_consulting = models.CharField(max_length=20, verbose_name='세부사항')

    vouchers =models.ImageField(
        upload_to='profile/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name='증빙자료첨부'
    )
    is_private = models.BooleanField(default=False, verbose_name='개인정보이용')
    is_agreement = models.BooleanField(default=False, verbose_name='서비스이용약관')
    is_sms = models.BooleanField(default=False, verbose_name='SMS광고수신')
    is_mentor_univ = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.name)

    def __unicode__(univ_categories):
        return univ_categories

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/accounts/no_profile_photo.png'
        return image_url

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class EmailConfirm(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='email_confirm',
        on_delete=models.CASCADE,
    )
    key = models.CharField(max_length=60)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)