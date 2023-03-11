from django.urls import path, include

from users.views import Register, Profile, Table
from users.views import ShowTable
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(),name='register'),
    path('Num1/', ShowTable.as_view(), name='table'),
    path('table/', Table.as_view(), name='year'),
    path('Profile/', Profile.as_view(), name='profile'),
]