# -*- coding: utf8 -*-
from app.news.models import News
from app.requests.forms import RequestForm
from app.requests.models import Request
from app.user.models import UserProfile
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.admin import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.views.generic import FormView, TemplateView
from django.views.generic.base import View
from forms import RegistrationForm


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "home/login.html"

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return next
        return '/home/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        if self.request.user.is_authenticated:
            return super(LoginFormView, self).form_valid(form)
        return super(LoginFormView, self).form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/home")


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = "home/registration.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/home")
        return super(RegistrationView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return '/login/?next=' + next
        return '/home'

    def form_valid(self, form):
        form_data = form.cleaned_data
        if form_data['request_id'] == 0:
            messages.add_message(self.request, messages.ERROR,
                                 u"А вы кто? Если вас нет в списке, обратитесь к администратору")
            return super(RegistrationView, self).form_invalid(form)
        user_email = form_data['email']
        request = Request.objects.filter(email=user_email).first()

        if not request:
            messages.add_message(self.request, messages.ERROR,
                                 u"Не найдена заявка с таким email")
            return super(RegistrationView, self).form_invalid(form)

        user_name = form_data['username']
        user_password_one = form_data['password_one']
        user_password_two = form_data['password_two']
        if user_password_one == user_password_two:
            user = User.objects.create_user(username=user_name,
                                            email=user_email,
                                            password=user_password_one)
            UserProfile(user=user, name=user_name, group=request.group,
                        email=user_email, sub_group=0, date_joined=now()).save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.add_message(self.request, messages.ERROR,
                                 u"Пароли не совпадают")
            return super(RegistrationView, self).form_invalid(form)
        return super(RegistrationView, self).form_valid(form)


class HomeCourseView(FormView):
    news_view_count = 2
    form_class = RequestForm
    success_url = '/thanks'

    def get_template_names(self):
        if self.request.user.is_authenticated():
            return 'home/home.html'
        return 'home/index.html'

    def get_context_data(self, **kwargs):
        kwargs['news'] = News.objects.all()[:self.news_view_count]
        return super(HomeCourseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        Request(**form.cleaned_data).save()
        return super(HomeCourseView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'home/thanks.html'


class RequestFailView(TemplateView):
    template_name = 'home/request_fail.html'
