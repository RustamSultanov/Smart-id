from django import forms
from . import models


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(label=("Password"),
                                       widget=forms.PasswordInput({
                                           'class': 'form-control',
                                           'placeholder': 'Password'}))


class EmployeeRegistrationForm(RegistrationForm):
    class Meta:
        model = models.Employee
        fields = ('email', 'phone_number', 'password', 'company', 'first_name', 'last_name', 'patronymic', 'sex')
        widgets = {'password': forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'})}


class SmartIdRegistrationForm(RegistrationForm):
    class Meta:
        model = models.SmartId
        fields = (
        'email', 'phone_number', 'password', 'first_name', 'last_name', 'patronymic', 'sex', 'description',
        'status', 'specialization')
        widgets = {'password': forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'})}


class BusinessSmartIdRegistrationForm(RegistrationForm):
    class Meta:
        model = models.BusinessSmartId
        fields = (
        'email', 'phone_number', 'password', 'company', 'first_name', 'last_name', 'patronymic', 'sex', 'company',
        'specialization')
        widgets = {'password': forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'})}
