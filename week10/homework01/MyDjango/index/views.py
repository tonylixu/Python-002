from django.shortcuts import render
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Django!")


def auth(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                username = cd['username']
                login(request, user)  
                return render(request, 'welcome.html', {'username': username})
            else:
                return HttpResponse('Login failed')

    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})
