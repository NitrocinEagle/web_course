# -*- coding: utf8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Event


class EventsAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        try:
            events = Event.objects.all()
        except:
            return Response({
                'result': 'error',
                'code': 1
            })
        events_response = []
        for event in events:
            events_response.append(
                {
                    'title': event.name,
                    'start': event.start.isoformat()[:19]
                }
            )
        return Response(events_response)
