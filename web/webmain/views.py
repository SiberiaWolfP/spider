# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from webmain.models import Baike


# Create your views here.
def index(requset):
    passages = Baike.objects.all()
    return render(requset,'index.html',{'passages':passages})