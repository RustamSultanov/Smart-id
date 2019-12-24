from django.contrib import admin

from .models import Employee, Company, SmartId, BusinessSmartId, Specialization, Account

admin.site.register(Account)
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(SmartId)
admin.site.register(BusinessSmartId)
admin.site.register(Specialization)
