# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import UserReg
import datetime
# Create your views here.


def index(request):
    users = UserReg.objects.all()
    if request.method == "POST":
        if "userAdd" in request.POST:
            first_name = request.POST["first name"]
            last_name = str(request.POST["last name"])
            age = request.POST["age"]
            job_position = request.POST["job position"]
            User = UserReg(first_name=first_name, last_name=last_name,
                        age=age, job_position=job_position)
            User.save()
            return redirect("/")

    return render(request, "index.html", {"users": users})
