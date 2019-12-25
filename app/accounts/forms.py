from django import forms
from . import models
from . import utils


class AccountRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(label=("Password"),
                                       widget=forms.PasswordInput({
                                           'class': 'form-control',
                                           'placeholder': 'Password'}))

    class Meta:
        model = models.User
        fields = (
            'email', 'phone_number', 'password', 'first_name', 'last_name', 'patronymic', 'sex', 'resident',
            'inn', 'photo', 'contacts')
        widgets = {'password': forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'})}

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError(
                "Пароли не совпадают!"
            )

    def save(self, commit=True):
        self.instance.set_password(self.cleaned_data['password'])
        result = self.instance.check_password(self.cleaned_data['password'])
        return super().save(commit)


class AccountAuthenticationForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = (
            'email', 'password')
        widgets = {'password': forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'})}

#
#
# class SmartIdRegistrationForm(RegistrationForm):
#     class Meta:
#         model = models.SmartId
#         fields = (
#             'email', 'phone_number', 'password', 'first_name', 'last_name', 'patronymic', 'sex', 'description',
#             'status', 'specialization')
#         widgets = {'password': forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'})}
#
#
# class BusinessSmartIdRegistrationForm(RegistrationForm):
#     tax_code = forms.CharField(label=("ИНН/ОГРН/ОГРНИП"), help_text="ИНН - 10 чисел, ОГРН - 13, ОГРНИП - 15")
#
#     class Meta:
#         model = models.BusinessSmartId
#         fields = (
#             'email', 'phone_number', 'password', 'first_name', 'last_name', 'patronymic', 'sex',
#             'specialization')
#         widgets = {'password': forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'})}
#
#     def save(self, commit=True):
#         tax_code = self.cleaned_data['tax_code']
#         json_file = utils.get_data_about_company_from_dadata(tax_code)
#         company = self.create_company_from_json(json_file)
#         self.instance.company = company
#         return super().save(commit)
#
#     @staticmethod
#     def create_company_from_json(json_file):
#         new_company = models.Company.objects.create(
#             name=json_file['suggestions'][0]['value'],
#             legal_address=json_file['suggestions'][0]['data']['address']["unrestricted_value"],
#             inn=json_file['suggestions'][0]['data']['inn'],
#             ogrn=json_file['suggestions'][0]['data']['ogrn'],
#             kpp=json_file['suggestions'][0]['data']['kpp'],
#             ceo=json_file['suggestions'][0]['data']['management']['name'],
#         )
#         return new_company
