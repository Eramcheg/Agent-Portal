from django.urls import path, include

from users.views import Register, Profile, Table, All_tables
from users.views import ShowTable
urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(),name='register'),
    path('de/Tables/', ShowTable.as_view(), name='table_de'),
    path('fr/Tables/', ShowTable.as_view(), name='table_fr'),
    path('it/Tables/', ShowTable.as_view(), name='table_it'),
    path('es/Tables/', ShowTable.as_view(), name='table_es'),
    path('en/Tables/', ShowTable.as_view(), name='table_en'),
    path('table/', Table.as_view(), name='year'),
    path('en/Profile/', Profile.as_view(), name='profile_en'),
    path('fr/Profile/', Profile.as_view(), name='profile_fr'),
    path('de/Profile/', Profile.as_view(), name='profile_de'),
    path('es/Profile/', Profile.as_view(), name='profile_es'),
    path('it/Profile/', Profile.as_view(), name='profile_it'),
    path('Global/', All_tables.as_view(), name='global'),

]