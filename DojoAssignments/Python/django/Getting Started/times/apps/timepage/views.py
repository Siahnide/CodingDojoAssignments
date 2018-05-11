# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect

from time import gmtime, strftime
# def index(request):
#   context = {
#   "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#   }
#   return render(request,'appname/index.html', context)


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'timepage/index.html', context)
# Create your views here.
