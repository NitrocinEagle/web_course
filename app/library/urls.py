from django.conf.urls import url, include
from .views import PePe

urlpatterns = [
    url(r'^api/', include('app.library.api.urls')),
    url(r'^main/$', PePe.as_view(), name='pepe')
]
