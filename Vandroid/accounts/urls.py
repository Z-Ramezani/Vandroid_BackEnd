from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [

    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]
