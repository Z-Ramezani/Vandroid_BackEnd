from django.urls import path
from . import views

app_name = 'activityComponents'
urlpatterns = [

    path('', views.ListActivityComponents.as_view(), name='activityComponents'),
]
