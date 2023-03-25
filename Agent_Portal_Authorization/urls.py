
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView

from users.views import Home, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    # path('', login_view, name='login'),
    path('users/', include('users.urls'))

]
urlpatterns+= staticfiles_urlpatterns()