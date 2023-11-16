from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.decorators import login_required

from .views import GetUserView, LogoutView, RegisterView, registro_usuario, inicio


urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('registro/', registro_usuario),
    path('inicio/', inicio),
    ]
