# -*- coding: utf8 -*-
from django.views.generic import TemplateView, ListView, FormView
from models import Task
from app.user.views import get_cntxt_data
from forms import NameForm


class TasksView(TemplateView):
    template_name = 'user/tasks/index.html'

    def get_context_data(self, **kwargs):
        return get_cntxt_data(self, **kwargs)


class AllTasksView(ListView):
    template_name = 'user/tasks/all.html'
    context_object_name = "all_tasks"

    def get_queryset(self):
        return Task.objects.filter(individual=False)

    def get_context_data(self, **kwargs):
        return get_cntxt_data(self, **kwargs)


class MyTasksView(ListView):
    template_name = 'user/tasks/my.html'
    context_object_name = "my_tasks"

    def get_queryset(self):
        return Task.objects.filter(users=self.request.user)

    def get_context_data(self, **kwargs):
        return get_cntxt_data(self, **kwargs)


class CompletedTasksView(TemplateView):
    template_name = 'user/tasks/completed.html'

    def get_context_data(self, **kwargs):
        return get_cntxt_data(self, **kwargs)


class SendTaskFormView(FormView):
    template_name = 'user/tasks/send_task.html'
    form_class = NameForm
    success_url = '/user/tasks/'

    def form_valid(self, form):
        answer_file = form.cleaned_data['answer_file']
        print answer_file
        return super(SendTaskFormView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        kwargs['user_id'] = self.kwargs.get('user_id')
        kwargs['task_id'] = self.kwargs.get('task_id')
        return get_cntxt_data(self, **kwargs)
