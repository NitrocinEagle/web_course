from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('app.about.urls')),
    url(r'^news/', include('app.news.urls')),
    url(r'^timetable/', include('app.timetable.urls')),
    url(r'^user/', include('app.user.urls', namespace='user')),
    url(r'^lectures/', include('app.lectures.urls')),
    url(r'^pos/', include('generic_positions.urls')),
    url(r'^survey/', include('multilingual_survey.urls')),
    url(r'^', include('app.home.urls', namespace='home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
