from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from cmunity.models import *

import os


#imageList = [filename for filename in os.listdir("static/gifs")]


class LoginPage(View):
    def get(self, request):
        return render(request,'login.html')


class RegistrationPage(View):
    def post(self, request):
        name = request.POST.get("Name")
        print("name: " + name)
        pw = "12345678"
        if (User.objects.filter(username=name).count() == 0):
            user = User.objects.create_user(name, "", pw)
            user.save()
            ud = UserData(andrewID=name)
            ud.save()
        user_login = authenticate(username=name, password=pw)
        login(request, user_login)
        return HttpResponseRedirect("/homepage")


class HomePage(View):
    def get(self, request):
        context = {}
        current_user = request.user
        username = current_user.username
        data = UserData.objects.get(andrewID=username)
        score = data.score
        context["score"] = score
        return render(request, 'game.html', context)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/login")
            #error message


class GpsStart(View):
    def get(self, request):
        context = {}
        current_user = request.user
        username = current_user.username
        data = UserData.objects.get(andrewID=username)
        score = data.score
        context["score"] = score
        return render(request, 'find.html', context)


class GifChoice(View):
    def get(self, request):
        context = {}
        current_user = request.user
        username = current_user.username
        data = UserData.objects.get(andrewID=username)
        data.score += 1
        data.save()
        score = data.score
        context["score"] = score
        return render(request, "win.html", context)


class GifChoiceWrong(View):
    def get(self, request):
        context = {}
        current_user = request.user
        username = current_user.username
        data = UserData.objects.get(andrewID=username)
        data.score += 1
        data.save()
        score = data.score
        context["score"] = score
        return render(request, "lose.html", context)


class CmuScores(View):
    def get(self, request):
        context = {}
        current_user = request.user
        username = current_user.username
        data = UserData.objects.get(andrewID=username)
        score = data.score
        context["score"] = score
        scoresDict = []
        for otheruser in UserData.objects.all():
            person = {"name": otheruser.andrewID, "score":otheruser.score}
            scoresDict.append(person)
        context["scores"] = scoresDict
        return render(request, 'score.html', context)




