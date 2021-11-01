from django.shortcuts import render
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

def index(request):
    return render(request, 'website/index.html') #returns the index.html

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("Please use correct id and password")
            # return HttpResponseRedirect(reverse('register'))

    else:
        return render(request, 'website/login.html')


def cloud(request):
    return render(request, 'website/cloud.html')

def security(request):
    template_name='website/security.html'
    return render(request, template_name)

def business_solution(request):
    return render(request, 'website/business_solution.html')

def ai_hub(request):
    return render(request, 'website/ai_hub.html')

def consulting(request):
    return render(request, 'website/consulting.html')
