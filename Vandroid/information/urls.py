from django.urls import path
from . import views

app_name = 'information'
urlpatterns = [

    path('', views.ListInfo.as_view(), name='information'),
]
