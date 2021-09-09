from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .models import *


class Login(LoginView):
    template_name = 'login.html'


class Signup(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")


def logout_view(request):
    logout(request)
    return redirect('/')



def index(request):
    if request.user.is_active:
        return render(request, 'welcome.html')
    else:
        return redirect('login/')
