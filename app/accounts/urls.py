from django.urls import path
from .views import SmartIdRegisterAPIView
app_name = "accounts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('registration', SmartIdRegisterAPIView.as_view(), name='registration'),

]