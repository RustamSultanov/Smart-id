from django.views.generic.edit import FormView
from django.conf import settings

from . import forms


class AccountRegistrationView(FormView):
    form_class = forms.AccountRegistrationForm
    success_url = settings.LOGIN_URL
    template_name = 'accounts/form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
