#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-27 09:52:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
