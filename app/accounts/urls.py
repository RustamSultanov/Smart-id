from django.urls import path
from .views import AccountRegistrationView
from main.views import login_view, UserAuthView

app_name = "accounts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('registration-employee', AccountRegistrationView.as_view(), name='registration_employee'),
    path('test', UserAuthView.as_view(), name='test')
]
