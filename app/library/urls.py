from django.conf.urls import url, include
from .views import TimetableView

urlpatterns = [
    url(r'^$', TimetableView.as_view()),
    url(r'^api/', include('app.library.api.urls')),
]
