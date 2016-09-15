# -*- coding: utf8 -*-
from django.db import connection
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
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


class EnterSurveyReportView(TemplateView):
    template_name = 'user/enter_survey_report.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/?next=/user/enter_survey/enter_survey/report/')
        return super(EnterSurveyReportView, self).get(request, *args, **kwargs)

    def get_survey_responses(self):
        with connection.cursor() as cursor:
            cursor.execute(
                '''SELECT  DISTINCT resp.user_id, req.name 'name', req.email 'email', req.social AS 'social',
quest_trans.title AS 'question', answ_trans.title AS 'answer', quest_trans.master_id AS 'question_id',
answ_trans.master_id AS 'answer_id' FROM multilingual_survey_surveyresponse resp
INNER JOIN multilingual_survey_surveyresponse_answer resp_answ ON resp.id = resp_answ.surveyresponse_id
INNER JOIN multilingual_survey_surveyquestion_translation quest_trans ON resp.question_id = quest_trans.master_id
INNER JOIN multilingual_survey_surveyanswer_translation answ_trans ON resp_answ.surveyanswer_id = answ_trans.master_id
INNER JOIN auth_user _user ON _user.id = resp.user_id
INNER JOIN requests_request req ON req.email = _user.email
WHERE answ_trans.title != '1'ORDER BY resp.user_id;''')
            row = cursor.fetchall()
        return row

    def get_context_data(self, **kwargs):
        right_responses = [(2, 5), (3, 9), (3, 9), (4, 12), (4, 13), (5, 17), (6, 20), (6, 22),
                           (7, 25), (7, 27), (8, 28), (8, 29), (8, 31), (9, 33), (9, 33), (11, 38), (12, 41)
                           ]
        responses = []
        extra_strange_answers = [u'система управления версиями', ]
        extra_strange_questions = [u'Базовым стеком протоколов интернет является', u'Кто такой Дима?']
        total_score = 0
        max_score = 17
        for r in self.get_survey_responses():
            if r[5] in extra_strange_answers or r[4] in extra_strange_questions:
                continue
            l = list(r)
            point = True if (r[6], r[7]) in right_responses else False
            l.append(point)
            responses.append(l)
            if r[0] == self.request.user.id and point:
                total_score += 1
        kwargs['responses'] = responses
        kwargs['max_score'] = max_score
        kwargs['total_score'] = total_score
        return super(EnterSurveyReportView, self).get_context_data(**kwargs)


class EnterSurveyReportAdminView(TemplateView):
    template_name = 'user/enter_survey_admin_report.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/home')
        return super(EnterSurveyReportAdminView, self).get(request, *args, **kwargs)

    def get_survey_responses(self):
        with connection.cursor() as cursor:
            cursor.execute(
                '''SELECT  DISTINCT resp.user_id, req.name 'name', req.email 'email', req.social AS 'social',
quest_trans.title AS 'question', answ_trans.title AS 'answer', quest_trans.master_id AS 'question_id',
answ_trans.master_id AS 'answer_id' FROM multilingual_survey_surveyresponse resp
INNER JOIN multilingual_survey_surveyresponse_answer resp_answ ON resp.id = resp_answ.surveyresponse_id
INNER JOIN multilingual_survey_surveyquestion_translation quest_trans ON resp.question_id = quest_trans.master_id
INNER JOIN multilingual_survey_surveyanswer_translation answ_trans ON resp_answ.surveyanswer_id = answ_trans.master_id
INNER JOIN auth_user _user ON _user.id = resp.user_id
INNER JOIN requests_request req ON req.email = _user.email
WHERE answ_trans.title != '1'ORDER BY resp.user_id;''')
            row = cursor.fetchall()
        return row

    def get_context_data(self, **kwargs):
        right_responses = [(2, 5), (3, 9), (3, 9), (4, 12), (4, 13), (5, 17), (6, 20), (6, 22),
                           (7, 25), (7, 27), (8, 28), (8, 29), (8, 31), (9, 33), (9, 33), (11, 38), (12, 41)
                           ]
        responses = []
        users_id = {}
        users_total_scores = {}
        users_other_answers = {}

        extra_strange_answers = [u'система управления версиями', ]
        extra_strange_questions = [u'Базовым стеком протоколов интернет является', ]

        max_score = 17
        for r in self.get_survey_responses():
            if r[5] in extra_strange_answers or r[4] in extra_strange_questions:
                continue
            if not users_id.get(str(r[0])):
                responses.append({
                    'id': r[0],
                    'data': {
                        'name': r[1],
                        'vk': r[3],
                        'mail': r[2],
                        'other_answer': SurveyResponse.objects.filter(user_id=r[0],
                                                                      question_id=10).first().other_answer,
                        'total_score': 0
                    },
                })
                users_id[str(r[0])] = True
                users_total_scores[str(r[0])] = 0
                users_other_answers[str(r[0])] = ''

            point = True if (r[6], r[7]) in right_responses else False

            if point:
                users_total_scores[str(r[0])] += 1

        for r in responses:
            r['data']['total_score'] = users_total_scores[str(r['id'])]

        kwargs['responses'] = sorted(responses, key=lambda resp: (-resp['data']['total_score']))
        kwargs['max_score'] = max_score
        return super(EnterSurveyReportAdminView, self).get_context_data(**kwargs)
