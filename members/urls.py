from django.urls import path
from .views import login_user, logout_user, register_user, ProfileUser

app_name = 'members'

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
    path('profile_user/<int:pk>/', ProfileUser.as_view(), name='profile_user'),
]