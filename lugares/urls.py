# -*- coding: utf-8 -*-
from django.conf.urls import url
from lugares import views

urlpatterns = [
    url(r'^$', views.lugares_list),
    url(r'^busca/nome/(?P<nome_busca>[\w , _]+)/endereco/(?P<endereco_busca>[\w , _.]+)/bairro/(?P<bairro_busca>[\w , _]+)/cidade/(?P<cidade_busca>[\w , _]+)/estado/(?P<estado_busca>[\w , _]+)/pais/(?P<pais_busca>[\w , _]+)/tags/(?P<tags_busca>[\w , _]+)/$', views.lugares_busca),
    url(r'^(?P<id>[0-9]+)/$', views.lugar),
    url(r'^reviews/(?P<id>[0-9]+)/$', views.reviews_lugar),
    url(r'^reviews/$', views.reviews_criar),
    url(r'^login/$', views.OnePageAppView.as_view(), name='home'),
]
from django.conf.urls import patterns, include, url

from . import views
