from django.urls import path
from . import views

app_name = 'ContentProvidersComponents'
urlpatterns = [
    path('', views.ListContentProvidersComponents.as_view(), name='dynamicRegisteredSerializer'),
]
