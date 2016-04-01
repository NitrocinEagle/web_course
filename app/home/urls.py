from django.conf.urls import url
from .views import LoginFormView, LogoutView, Home1AprilView,HomeCourseView

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^home/$', Home1AprilView.as_view()),
    url(r'^home_course/$', HomeCourseView.as_view(), name='index'),
    url(r'^$', LoginFormView.as_view()),
]
