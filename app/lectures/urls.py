from django.conf.urls import url
from .views import LecturesView

urlpatterns = [
    url(r'^$', LecturesView.as_view()),
]


