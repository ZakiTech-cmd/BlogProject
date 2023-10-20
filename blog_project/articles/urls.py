from django.urls import path

from .views import *

urlpatterns = [
    path("api/login/", LoginAPI.as_view(), name="login_api"),
    path("api/logout/", LogoutAPI.as_view(), name="logout_api"),
]
