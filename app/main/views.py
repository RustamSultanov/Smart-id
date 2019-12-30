from django.shortcuts import render
import logging
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.
logger = logging.getLogger(__name__)


class UserAuthView(FormView):
    form_class = LoginForm
    success_url = settings.LOGIN_URL
    template_name = 'accounts/form.html'

    def get_context_data(self, **kwargs):
        user = get_user_model()
        x = user.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):

        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(email=email, password=password)
        if login_user:
            auth_login(self.request, login_user)
            return super().form_valid(form)


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(email=email, password=password)
        if login_user:
            auth_login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)