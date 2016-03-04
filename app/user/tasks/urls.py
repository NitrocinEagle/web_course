from django.conf.urls import url
from .views import AllTasksView, MyTasksView, TasksView, CompletedTasksView, SendTaskFormView

urlpatterns = [
    url(r'^all/$', AllTasksView.as_view()),
    url(r'^my/$', MyTasksView.as_view()),
    url(r'^completed/$', CompletedTasksView.as_view()),
    url(r'^send_task/(?P<task_id>\d+)/(?P<user_id>\d+)/$', SendTaskFormView.as_view()),
    url(r'^$', TasksView.as_view()),
]
