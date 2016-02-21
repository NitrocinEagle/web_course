from django.conf.urls import url
from .views import UserProfileView, UserTasksView

urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view()),
    url(r'^tasks/$', UserTasksView.as_view()),
]


