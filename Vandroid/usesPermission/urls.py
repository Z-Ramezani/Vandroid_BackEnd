from django.urls import path
from . import views

app_name = 'usesPermission'
urlpatterns = [

    path('', views.ListUsesPermission.as_view(), name='usesPermission'),
]
