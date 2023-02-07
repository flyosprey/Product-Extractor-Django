from django.urls import path

from .views import ServiceView


urlpatterns = [
    path("", ServiceView.as_view(), name="service")
]
