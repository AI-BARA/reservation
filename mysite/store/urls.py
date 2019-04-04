from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^expline/$', views.expline, name='expline'),
    url(r'^admin/$', views.index, name='index'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^login/$', views.login, name='login'),
    url(r'^order/$', views.order, name='add'),
    url(r'^maker/$', views.maker1, name='maker'),
    url(r'^maker-list/$', views.maker_list, name='maker_list'),
    url(r'^makedelete/$', views.makedelete, name='make_delete'),
    url(r'^entrance-list/$', views.entrance_list, name='entrance_list'),
    url(r'^entrance0/$', views.entrance0, name='entrance0'),
    url(r'^entrance1/$', views.entrance1, name='entrance1'),
    url(r'^entrance3/$', views.entrance1, name='entrance3'),
]
