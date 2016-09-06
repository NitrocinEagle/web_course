# -*- coding: utf8 -*-
from app.faq.models import FAQ
from app.news.models import News
from app.requests.forms import RequestForm
from app.requests.models import Request
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.views.generic.base import View


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "home/login.html"
    success_url = "/home"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/home")


class HomeCourseView(FormView):
    template_name = 'home/index.html'
    news_view_count = 2
    form_class = RequestForm
    success_url = '/thanks'

    def get_context_data(self, **kwargs):
        kwargs['news'] = News.objects.all()[:self.news_view_count]
        kwargs['faqs'] = FAQ.objects.all()
        return super(HomeCourseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        Request(**form.cleaned_data).save()
        return super(HomeCourseView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'home/thanks.html'
