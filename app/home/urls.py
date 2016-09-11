from django.conf.urls import url
from .views import (LoginFormView, LogoutView, HomeCourseView, ThanksView,
                    RegistrationView, RequestFailView)

urlpatterns = [
    url(r'^registration/$', RegistrationView.as_view()),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^home/$', HomeCourseView.as_view()),
    url(r'^thanks/$', ThanksView.as_view()),
    url(r'^request_fail/$', RequestFailView.as_view()),
    url(r'^$', HomeCourseView.as_view()),
]
