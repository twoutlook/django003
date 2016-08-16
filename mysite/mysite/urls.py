from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^app2/', include('app2.urls')),
    url(r'^app001/', include('app001.urls')),
    url(r'^f1/', include('f1.urls')),
    url(r'^f2/', include('f2.urls')),
    url(r'^materials/', include('materials.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
