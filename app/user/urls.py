from django.conf.urls import url, include
from .views import UserProfileView, AchievmentsView, UserSettingsView

urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view()),
    url(r'^achievments/$', AchievmentsView.as_view()),
    url(r'^settings/$', UserSettingsView.as_view()),
    url(r'^tasks/', include('app.user.tasks.urls')),
    url(r'^$', UserProfileView.as_view()),
]
