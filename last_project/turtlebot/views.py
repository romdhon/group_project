from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'turtlebot/home.html'

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('User is not active')
    
    else:
        return render(request, template_name="turtlebot/login.html")

@login_required
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def getting_start(request):
    msg = "Getting Start!"
    return render(request, 'turtlebot/content/getting_start/getting_start.html', {
        "msg":msg
    })
        

