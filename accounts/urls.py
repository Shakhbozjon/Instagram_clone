from django.urls import path
from .views import user_login, dashboard_view, SignUpView, user_register, edit_user, index
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from accounts import views



urlpatterns = [
    # path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', user_login, name='login'),
    path('profile/', dashboard_view, name='user_profile'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', user_register, name='signup'),
    path('profile/edit/', edit_user, name='edit_user'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/ ', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]