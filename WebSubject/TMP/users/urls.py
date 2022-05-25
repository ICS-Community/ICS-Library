from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(success_url='/'), name='login', kwargs={'authentication_form': LoginForm}),
    path('register/', views.RegisterView.as_view(success_url="/"), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('account/result.html', views.account_result, name='result'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('forget_password_code/', views.ForgetPasswordEmailCode.as_view(), name='forget_password_code'),

]