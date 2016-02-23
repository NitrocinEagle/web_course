from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('app.about.urls')),
    url(r'^news/', include('app.news.urls')),
    url(r'^timetable/', include('app.timetable.urls')),
    url(r'^user/', include('app.user.urls')),
    url(r'^', include('app.home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
