from django.urls import path
from .views import login_user, logout_user, register_user, ProfileUser, verify_email, CustomPasswordResetView, \
    CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name = 'members'

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
    path('profile_user/<int:pk>/', ProfileUser.as_view(), name='profile_user'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', verify_email,
         name='activate'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]