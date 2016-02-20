from django.conf.urls import url
from .views import TimetableView

urlpatterns = [
    url(r'^$', TimetableView.as_view()),
]
