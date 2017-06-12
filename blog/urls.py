from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^reachme$', views.reachme, name='reachme'),
    url(r'^(?P<url>\w+)$', views.post_detail, name='post_detail'),
]