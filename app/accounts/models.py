from django.db import models

from main.models import User


class Specialization(models.Model):
    name = models.CharField(verbose_name='Название специализации', max_length=100)

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    legal_address = models.CharField(verbose_name='Юридический адрес', max_length=100)
    inn = models.CharField(verbose_name='ИНН', max_length=100)
    ogrn = models.CharField(verbose_name='ОГРН', max_length=100)
    kpp = models.CharField(verbose_name='КПП', max_length=100)
    ceo = models.CharField(verbose_name='CEO', max_length=100)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Аккаунт')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'employee'


class SmartId(models.Model):
    STATUS_CHOICE = ((0, 'Физическое лицо'), (1, 'Самозанятый'), (2, 'Официально работающий'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Аккаунт')
    description = models.CharField(verbose_name='Описание', max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0, verbose_name='Статус физического лица')
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, verbose_name='Специализация')
    passport_scan = models.ImageField(blank=True, null=True, verbose_name='Скан паспорта')

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'smart_id'


class BusinessSmartId(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Аккаунт')
    company = models.OneToOneField(Company, on_delete=models.PROTECT, verbose_name='Компания')
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, verbose_name='Специализация')

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'business_smart_id'
