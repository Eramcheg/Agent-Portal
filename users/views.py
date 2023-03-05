import shutil
import urllib.request
from contextlib import closing

from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreationForm


class ShowTable(View):
    template_name = 'Cabine.html'
    # with closing(urllib.request.urlopen('ftp://admin:admin1234@192.168.56.1/')) as r:
    #     with open('OutputResult249.xlsx', 'wb') as f:
    #         shutil.copyfileobj(r, f)
    link = 'ftp://admin:admin1234@192.168.56.1/OutputResult249.xlsx'

    def get(self, request):
        return render(request, self.template_name)
class Profile(View):
    template_name = 'Profile.html'
    def get(self, request):
        return render(request, self.template_name)

class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user= authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)

