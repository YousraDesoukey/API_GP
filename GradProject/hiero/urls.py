from django.conf.urls import url
from hiero import views

urlpatterns = [
     url(r'^image/$', views.ImageView.as_view()),
]
