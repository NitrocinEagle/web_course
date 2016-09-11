# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from multilingual_survey.models import SurveyResponse
from multilingual_survey.views import SurveyView


class EnterSurveyView(SurveyView):
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            kwargs['has_passed'] = True if SurveyResponse.objects.filter(
                user=self.request.user) else False
        return super(EnterSurveyView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(EnterSurveyView, self).get(request, *args, **kwargs)
        return HttpResponseRedirect('/registration/?next=' + request.path)