from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^test$', views.test, name='test'),
    url(r'^Query$', views.Query, name='Query'),
 ]
