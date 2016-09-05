# -*- coding: utf-8 -*-
from django import forms

ATTRS = {'class': 'form-control bg-dark'}


class RequestForm(forms.Form):
    name = forms.CharField(max_length=256, label=u'Как вас зовут?',
                           help_text=u'Василий Пупкин')
    group = forms.CharField(max_length=256, label=u'В какой группе вы учитесь?',
                            help_text=u'КИ14-098')
    email = forms.CharField(max_length=60, label=u'Ваш почтовый адрес?',
                            help_text=u'v_pupkin@mail.ru')
    social = forms.CharField(max_length=60,
                             label=u'Страничка из социальных сетей',
                             help_text=u'vk.com/v_pupkin')
