from django.urls import path
from .views import AccountRegistrationView

app_name = "accounts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('registration-employee', AccountRegistrationView.as_view(), name='registration_employee'),
]
