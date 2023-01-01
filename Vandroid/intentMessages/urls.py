from django.urls import path
from . import views

app_name = 'intentMessages'
urlpatterns = [

    path('', views.ListIntentMessages.as_view(), name='intentMessages'),
]
