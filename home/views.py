from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "home/signup_page.html"
    success_url = "/service"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/admin")
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"
