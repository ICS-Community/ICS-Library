from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.Logout, name='logout'),
    path('<int:u_id>/', views.User_detail, name='user_detail'),
    path('<int:u_id>/manage/', views.User_manage, name='user_manage'),
    path('<int:u_id>/book_list/<int:bf_id>/', views.Book_list, name='ubook_list')
]
