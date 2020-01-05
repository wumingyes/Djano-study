#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-27 10:14:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	# path('login/',views.user_login,name='login'),
	path('login/',auth_views.LoginView.as_view(),name='login'),
	path('logout/',auth_views.LogoutView.as_view(),name='logout'),
	path('',views.dashboard,name='dashboard'),
	path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
	path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
	]
