# -*- coding: utf-8 -*-
from django import forms


class NameForm(forms.Form):
    answer_file = forms.FileField(label='Answer file', help_text=u'Вспомогательный текст')
