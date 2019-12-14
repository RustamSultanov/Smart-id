from django.db import models

from ..main.models import BaseSmartId, Account


class Company(models.Model):
    name = models.CharField(verbose_name='Название')
    legal_address = models.CharField(verbose_name='Юридический адрес')
    inn = models.CharField(verbose_name='ИНН')
    ogrn = models.CharField(verbose_name='ОГРН')
    kpp = models.CharField(verbose_name='КПП')
    ceo = models.CharField(verbose_name='CEO')

    def __str__(self):
        return f'{self.name}'


class Employee(Account):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class SmartId(BaseSmartId):
    STATUS_CHOICE = ((0, 'Физическое лицо'), (1, 'Самозанятый'), (2, 'Официально работающий'))

    description = models.CharField(verbose_name='Описание')
    status = models.IntegerField(choices=STATUS_CHOICE, default=0, verbose_name='Статус физического лица')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class BusinessSmartId(BaseSmartId):
    company = models.OneToOneField(Company, on_delete=models.PROTECT, verbose_name='Компания')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
