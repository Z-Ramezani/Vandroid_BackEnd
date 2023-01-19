from django.urls import path
from . import views

app_name = 'activityAliasComponents'
urlpatterns = [

    path('', views.ListActivityAliasComponents.as_view(), name='activityComponents'),
]
