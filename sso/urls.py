from django.urls import path

from sso import views

urlpatterns = [
    path("", views.view_index, name="index"),
    path("accessibilite/", views.view_accessibilite, name="accessibilite"),
    path("accounts/login/", views.view_login, name="login"),
]
