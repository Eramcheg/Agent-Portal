
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView

from users.views import Home, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home_en'),
    # path('', login_view, name='login'),
    path('users/', include('users.urls')),
    path('de/', Home.as_view(), name='home_de'),
    path('fr/', Home.as_view(), name='home_fr'),
    path('es/', Home.as_view(), name='home_es'),
    path('it/', Home.as_view(), name='home_it'),
]
urlpatterns+= staticfiles_urlpatterns()