"""URLs for the multilingual_survey app."""
from django.conf.urls import url

from views import EnterSurveyView


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', EnterSurveyView.as_view(), name='enter_test'),
]
