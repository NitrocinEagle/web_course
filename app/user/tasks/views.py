# -*- coding: utf8 -*-
import os
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
    valid_formats = [".jpg", ".png", ".jpeg", ".rar", ".zip", ".txt"]
    msg = {
        'upload': u"Файл с ответом был успешно загружен!",
        'update': u"Загрузили новый файл с ответом.",
        'over_size': u"Максимальный размер файла - 10 Mb.",
        'invalid_format': u"Неверный формат файла.",
        'file_not_load': u"Вы забыли загрузить файл.",
        'empty': u"Файл пустой."
    }
    max_upload_size = 10485760  # 10 Mb

    def get_success_url(self):
        return "/user/tasks/send_task/%s/%s" % (
            self.kwargs.get('task_id'), self.kwargs.get('user_id'))

    def form_valid(self, form):
        task = Task.objects.get(id=self.kwargs.get('task_id'))
        answer_file = self.request.FILES.get('answer_file')
        user = self.request.user

        ext = os.path.splitext(answer_file.name)[1]
        if not ext in self.valid_formats:
            messages.add_message(self.request, messages.WARNING,
                                 self.msg['invalid_format'])
            return super(SendTaskFormView, self).form_valid(form)

        answer_file_size = answer_file.size
        if answer_file_size > self.max_upload_size:
            messages.add_message(self.request, messages.WARNING,
                                 self.msg['over_size'])
            return super(SendTaskFormView, self).form_valid(form)

        try:
            answer = TaskAnswer.objects.get(task=task, user=self.request.user)
            answer.answer_file = answer_file
            answer.save()
            messages.add_message(self.request, messages.INFO,
                                 self.msg['update'])
        except:
            answer = TaskAnswer(
                answer_file=answer_file,
                task=task,
                user=user
            )
            answer.save()
            messages.add_message(self.request, messages.SUCCESS,
                                 self.msg['upload'])
        return super(SendTaskFormView, self).form_valid(form)

    def form_invalid(self, form):
        answer_file = self.request.FILES.get('answer_file', None)
        if not answer_file:
            messages.add_message(self.request, messages.WARNING,
                                 self.msg['file_not_load'])
        else:
            if answer_file.size is 0:
                messages.add_message(self.request, messages.WARNING,
                                     self.msg['empty'])
        return super(SendTaskFormView, self).form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        kwargs['task'] = Task.objects.get(id=kwargs.get('task_id'))
        try:
            kwargs['answer'] = TaskAnswer.objects.get(
                user_id=kwargs.get('user_id'),
                task_id=kwargs.get('task_id')
            )
        except:
            pass
        return super(SendTaskFormView, self).get_context_data(**kwargs)
