from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),

    # path('', views.home, name='home'),
    # path('checkview', views.checkview, name='checkview'),
    path('', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/', views.getMessages, name='getMessages'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html") , name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="done.html"),name='password_reset_complete'),
]