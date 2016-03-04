from django import forms


class NameForm(forms.Form):
    answer_file = forms.FileField(label='Answer file', help_text='max. 42 megabytes')
