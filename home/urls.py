from django.urls import path

from .views import SignupView, LoginInterfaceView, LogoutInterfaceView, HomeView


urlpatterns = [
    path("login/", LoginInterfaceView.as_view(), name="login"),
    path("logout/", LogoutInterfaceView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("", HomeView.as_view(), name="home")
]
