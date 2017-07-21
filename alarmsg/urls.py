from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    # url(r'^data/(?P<id>\d+)/$', views.data),
    url(r'^update/', views.update),
    url(r'^recent/', views.fetch_recent),
    url(r'^subworks/(?P<loc>\d+)/$', views.subworks, name='subworks'),
    # url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    # url(r'^regist/$', views.regist, name='regist'),
    url(r'^category/(?P<cat>.+)/$', views.categories, name='category'),
    url(r'^summary/$', views.summary, name='summary'),
    url(r'^query/$', views.query_view, name='query'),
    url(r'^querystart/(?P<loc>\d+)/(?P<rec>\d+)/(?P<cat>\d+)/$', views.query_start, name='query_start'),
    # url(r'^querystart/(?P<loc>\d+)/$', views.query_start, name='query_start'),
    url(r'^setup/', views.setup, name='setup'),
    url(r'^locedit/(?P<locid>\d+)/$', views.loc_edit, name='loc_edit'),
    # url(r'^locupdate/$', views.loc_update, name='loc_update'),
    url(r'^locadd/$', views.loc_add, name='loc_add'),
    url(r'^locdel/(?P<locid>\d+)/(?P<action>.+)/$', views.loc_del, name='loc_del'),
]
