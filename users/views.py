import ftplib
import os.path
import shutil
import urllib.request
from contextlib import closing

import wget
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.views import View
from openpyxl import load_workbook
from users.forms import UserCreationForm




class All_tables(View):
    def get(self, request):

        context = {'is_home_page': False,
                   'is_tables_page': False,
                   'is_profile_page': False,
                   'is_all_tables_page': True,
                   'is_authenticated': request.user.is_authenticated
                   }
        return render(request,'All_Tables.html', context)

class Table(View):
    def get(self, request):

        if request.user.is_authenticated:

            username = str(request.user.username)
            print(username)

            name_html = username + "_" + str(request.GET.get('name'))
            print(name_html)
            trueOrFalse = self.create_table(name_html)
            if trueOrFalse:
                return render(request, name_html+'.html')
            else:
                return render(request, 'NotFoundHtml.html')
        else:
            return render(request, 'NotFoundHtml.html')
    def create_table(self, name_html):
        try:
            link = f'ftp://admin:admin1234@192.168.56.1/{name_html}.xlsx'

            with urllib.request.urlopen(link) as response, open(f"{name_html}.xlsx", 'wb') as out_file:
                data = response.read()  # Read the contents of the file
                out_file.write(data)  # Write the contents to the local file

            wb = load_workbook(f'{name_html}.xlsx')
            ws = wb['Sheet']
            html = """<meta charset="utf-8">
             <table border="1" class="dataframe">
                         <thead>
                             <tr style="text-align: right;">\n"""
            k = 0

            for i in ws.iter_rows():
                if k > 0:
                    html += '<tr>\n'
                for j in range(len(i)):
                    value = str(i[j].value)
                    color = str(i[j].fill.start_color.rgb)
                    if (value == 'None'):
                        value = ' '
                    if color == '00000000':
                        color = 'FFFFFFFF'

                    if k < 1:
                        html += "<th style='background-color: #" + color[2:8] + "'>" + value + "</th>\n"
                    else:
                        html += "<td style='background-color: #" + color[2:8] + "'>" + value + "</td>\n"
                html += '</tr>\n'
                if k < 1:
                    html += """</thead>
              <tbody>"""
                k += 1
            html += """ </tbody>
            </table>"""
            html.encode('UTF-8')
            with open('templates/'+name_html+".html", 'w', encoding='utf-8') as f:
                f.write(html)
                return True
        except :
            return False


class Home(View):
    def get(self, request):
        is_auth = request.user.is_authenticated
        context = {'is_home_page': True,
                   'is_tables_page': False,
                   'is_profile_page':False,
                   'is_all_tables_page': False,
                   'is_authenticated': is_auth
                   }
        return render(request, 'home.html', context)

class ShowTable(View):
    template_name = 'Cabine.html'


    def get(self, request):
        if request.user.is_authenticated:
            username = str(request.user.username)
            print(username)
        is_auth = request.user.is_authenticated
        context = {'is_home_page': False,
                   'is_tables_page': True,
                   'is_profile_page': False,
                   'is_all_tables_page': False,

                   'is_authenticated': is_auth}

        print(str(request.GET.get('name')))

        return render(request, self.template_name, context)


class Profile(View):
    template_name = 'Profile.html'

    def get(self, request):
        is_auth = request.user.is_authenticated
        context = {'is_home_page': False,
                   'is_tables_page': False,
                   'is_all_tables_page': False,
                   'is_profile_page': True,
                   'is_authenticated': is_auth
                   }
        return render(request, self.template_name, context)

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

