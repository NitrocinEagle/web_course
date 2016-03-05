# -*- coding: utf8 -*-
from django.views.generic import ListView, FormView
from django.contrib import messages
from app.user.views import UserViewBase, UserProfile
from models import Task, TaskAnswer
from forms import NameForm


class TasksView(UserViewBase):
    template_name = 'user/tasks/index.html'


class AllTasksView(ListView):
    template_name = 'user/tasks/all.html'
    context_object_name = "all_tasks"

    def get_queryset(self):
        return Task.objects.filter(individual=False)

    def get_context_data(self, **kwargs):
        kwargs['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return super(AllTasksView, self).get_context_data(**kwargs)


class MyTasksView(ListView):
    template_name = 'user/tasks/my.html'
    context_object_name = "my_tasks"

    def get_queryset(self):
        return Task.objects.filter(users=self.request.user)

    def get_context_data(self, **kwargs):
        kwargs['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return super(MyTasksView, self).get_context_data(**kwargs)


class CompletedTasksView(UserViewBase):
    template_name = "user/tasks/completed.html"


class SendTaskFormView(UserViewBase, FormView):
    template_name = "user/tasks/send_task.html"
    form_class = NameForm

    def get_success_url(self):
        return "/user/tasks/send_task/%s/%s" % (
            self.kwargs.get('task_id'), self.kwargs.get('user_id'))

    def form_valid(self, form):
        try:
            answer = TaskAnswer.objects.get(
                task=Task.objects.get(id=self.kwargs['task_id']),
                user=self.request.user
            )
            answer.answer_file = self.request.FILES['answer_file']
            answer.save()
            messages.add_message(self.request, messages.INFO,
                                 u'Загрузили новый файл с ответом, удалив старый.')
        except:
            answer = TaskAnswer(
                answer_file=self.request.FILES['answer_file'],
                task=Task.objects.get(id=self.kwargs['task_id']),
                user=self.request.user
            )
            answer.save()
            messages.add_message(self.request, messages.SUCCESS,
                                 u'Файл с ответом был успешно загружен!')
        return super(SendTaskFormView, self).form_valid(form)

    def form_invalid(self, form):
        if not self.request.FILES.get('answer_file', None):
            messages.add_message(self.request, messages.WARNING,
                                 u'Загрузите файл с ответом!')
        return super(SendTaskFormView, self).form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        kwargs['user_id'] = self.kwargs.get('user_id')
        kwargs['task_id'] = self.kwargs.get('task_id')
        kwargs['task'] = Task.objects.get(id=kwargs['task_id'])
        try:
            kwargs['answer'] = TaskAnswer.objects.get(
                user_id=kwargs['user_id'],
                task_id=kwargs['task_id']
            )
        except:
            pass
        return super(SendTaskFormView, self).get_context_data(**kwargs)
