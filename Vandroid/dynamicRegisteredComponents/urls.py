from django.urls import path
from . import views

app_name = 'dynamicRegisteredComponents'
urlpatterns = [
    path('', views.ListDynamicRegisteredComponents.as_view(), name='dynamicRegisteredSerializer'),
]
