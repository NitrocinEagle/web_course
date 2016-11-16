"""URLs for the multilingual_survey app."""
from django.conf.urls import url

from .views import EnterSurveyView, EnterSurveyReportView, EnterSurveyReportAdminView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', EnterSurveyView.as_view(), name='enter_test'),
    url(r'^(?P<slug>[\w-]+)/report/$', EnterSurveyReportView.as_view(), name='report'),
    url(r'^(?P<slug>[\w-]+)/report-admin/$', EnterSurveyReportAdminView.as_view(), name='report_admin'),
]
