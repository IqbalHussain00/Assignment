from django.urls import path
from .views import *
from .apiviews import LoginAPI,RegisterAPI,logout


urlpatterns = [
    path('', home , name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout),
    path('login/login_api/', LoginAPI.as_view()),
    path('register/register_api/', RegisterAPI.as_view())
]