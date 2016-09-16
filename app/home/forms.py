# -*- coding: utf-8 -*-
from app.requests.models import Request
from django import forms


def get_requests_choices():
    requests = [(0, u'-------')]
    [requests.append((req.id, req)) for req in Request.objects.all().order_by(name)]
    return requests


class RegistrationForm(forms.Form):
    request_id = forms.ChoiceField(label=u'Кто вы?', required=False,
                                   choices=get_requests_choices())
    username = forms.CharField(label=u'Придумайте логин',
                               help_text=u'VPupkin-KI14', required=True)
    email = forms.CharField(label=u'Email, указанный в заявке',
                            help_text=u'v_pupkin@mail.ru')
    password_one = forms.CharField(label=u'Пароль', help_text=u'123qwerty',
                                   required=True)
    password_two = forms.CharField(label=u'Повторите пароль',
                                   help_text=u'123qwerty', required=True)
