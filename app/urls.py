from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('app.about.urls')),
    url(r'^news/', include('app.news.urls')),
    url(r'^timetable/', include('app.timetable.urls')),
    url(r'^', include('app.home.urls')),
]
