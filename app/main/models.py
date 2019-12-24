from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class AccountManager(BaseUserManager):
    # TODO: вероятно метод не рабочий, не создаются значения для прочих обязательных полей
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)


class BaseAccount(AbstractBaseUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = AccountManager()

    SEX_CHOICE = ((0, 'Мужской'), (1, 'Женский'))

    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(unique=True, verbose_name='Номер телефона', max_length=100)
    password = models.CharField(verbose_name='Пароль', max_length=100)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(blank=True, null=True, verbose_name='Отчество', max_length=100)
    sex = models.IntegerField(choices=SEX_CHOICE, default=0, verbose_name='Пол')

    class Meta:
        abstract = True



