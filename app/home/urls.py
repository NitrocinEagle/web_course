from django.conf.urls import url, include
from django.contrib import admin
from .views import LoginFormView, LogoutView, HomeView

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^home/$', HomeView.as_view()),
    url(r'^$', LoginFormView.as_view()),
]
