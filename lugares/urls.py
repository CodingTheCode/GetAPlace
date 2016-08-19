# -*- coding: utf-8 -*-
from django.conf.urls import url
from lugares import views

urlpatterns = [
    url(r'^$', views.lugares_list),

]
