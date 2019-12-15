from django.urls import path
from .views import SmartIdRegisterAPIView, EmployeeRegisterAPIView
app_name = "accounts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('registration-smart-id', SmartIdRegisterAPIView.as_view(), name='registration_smart_id'),
    path('registration-employee', EmployeeRegisterAPIView.as_view(), name='registration_employee'),
]