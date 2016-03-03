from django.conf.urls import url
from .views import AllTasksView, MyTasksView, TasksView, CompletedTasksView

urlpatterns = [
    url(r'^all/$', AllTasksView.as_view()),
    url(r'^my/$', MyTasksView.as_view()),
    url(r'^completed/$', CompletedTasksView.as_view()),
    url(r'^$', TasksView.as_view()),
]
