from django.conf.urls import url, include
from django.contrib import admin
from hiero import urls as hiero

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/hiero/', include(hiero)),
]
