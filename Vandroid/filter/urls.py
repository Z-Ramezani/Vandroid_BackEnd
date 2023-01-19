from django.urls import path
from . import views

app_name = 'filter'
urlpatterns = [

    path('', views.ListFilterComponents.as_view(), name='filter'),
]
