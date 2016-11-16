from django.conf.urls import url
from .views import LecturesView, LessonView

urlpatterns = [
    url(r'^$', LecturesView.as_view()),
    url(r'lesson/(?P<lesson_num>\d+)$', LessonView.as_view()),
]
