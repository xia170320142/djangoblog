# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from datetime import datetime

def home(request):
	post_list = Blog.objects.all()
	return render(request, 'home.html', {'post_list':post_list})

# Create your views here.
