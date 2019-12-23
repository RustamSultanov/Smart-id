from django.urls import path
from .views import EmployeeRegistrationView

app_name = "accounts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('registration-employee', EmployeeRegistrationView.as_view(), name='registration_employee'),
    path('registration-smart-id', EmployeeRegistrationView.as_view(), name='registration_smart_id'),
    path('registration-business-smart-id', EmployeeRegistrationView.as_view(), name='registration_business_smart_id'),
]
