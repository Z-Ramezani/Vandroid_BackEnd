from django.urls import path
from . import views

app_name = 'broadcastReceiversComponents'
urlpatterns = [

    path('', views.ListBroadcastReceiversComponents.as_view(), name='broadcastReceiversComponents'),
]
