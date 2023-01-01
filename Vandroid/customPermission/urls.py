from django.urls import path
from . import views

app_name = 'customPermission'
urlpatterns = [

    path('', views.ListCustomPermission.as_view(), name='customPermission'),
]
