from django.urls import path
from .views import register, user_login, user_logout, get_csrf_token

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('csrf/', get_csrf_token, name='csrf'),
]