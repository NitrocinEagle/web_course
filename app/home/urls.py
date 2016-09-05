from django.conf.urls import url
from .views import LoginFormView, LogoutView, HomeCourseView, ThanksView

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^home/$', HomeCourseView.as_view()),
    url(r'^thanks/$', ThanksView.as_view()),
    url(r'^$', HomeCourseView.as_view()),
]
