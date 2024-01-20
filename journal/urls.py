from django.urls import path

from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage,name=''),

    path('register/',views.register,name='register'),
    
    path('login/',views.login,name='login'),
    
    path('dashboard/',views.dashboard,name='dashboard'),

    path('logout/',views.logout,name='logout'),

    path('create_thought/',views.create_thought,name='create_thought'),

    path('my_thought/',views.my_thought,name='my_thought'),

    path('update_thought/<str:pk>/',views.update_thought,name='update_thought'),

    path('delete_thought/<str:pk>/',views.delete_thought,name='delete_thought'),

    path('profile_management/',views.profile_management,name='profile_management'),

    path('delete_account/',views.delete_account,name='delete_account'),


#   Password Management 
    # 1 -Allow us to enter our email in order to receive a password reset link

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='journal/password-reset.html'), name ='reset_password'),

    # 2 - Show a success Message stating that an email was sent to reset our Password

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='journal/password-reset-sent.html'),name='password_reset_done'),

    # 3 - Send a link to our email, so that we can reset our password

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='journal/password-reset-form.html'),name='password_reset_confirm'),

    # 4 - show a success message that our password is changed

    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='journal/password-reset-completed.html'),name='password_reset_complete')



]
