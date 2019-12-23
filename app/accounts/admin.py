from django.contrib import admin

from .models import Employee, Company, SmartId, BusinessSmartId

admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(SmartId)
admin.site.register(BusinessSmartId)

