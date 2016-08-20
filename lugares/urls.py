# -*- coding: utf-8 -*-
from django.conf.urls import url
from lugares import views

urlpatterns = [
    url(r'^$', views.lugares_list),
    url(r'^busca/(?P<nome_busca>[\w ]+)/$', views.lugares_busca)
    # url(r'^$', views.lugares_list),
]
