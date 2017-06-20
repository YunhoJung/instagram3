from django.conf.urls import url

from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$/', views.post_list, name='post_list'),
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_pk>[0-9]+)/$', views.post_delete, name='post_delete'),
]