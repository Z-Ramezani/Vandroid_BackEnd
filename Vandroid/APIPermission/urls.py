from django.urls import path
from . import views

app_name = 'APIpermission'
urlpatterns = [

    path('', views.ListAPIPermission.as_view(), name='APIPermission'),
]
