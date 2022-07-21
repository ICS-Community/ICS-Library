from django.urls import path
from . import views

app_name = 'forum'

"""这个程序是主程序，此路由为主路由"""
urlpatterns = [
    path('', views.index, name='index'),
    # 论坛首页
    path('forum/', views.forum, name='forum'),
    # 某标签的详细页面 专区
    path('t/<str:tid>/', views.tag_detail, name='tag_detail'),
    # 帖子详情页面
    path('forum/topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    # 用于添加帖子的页面
    path('forum/add_topic/', views.add_topic, name='add_ftopic'),
    path('forum/add_topic/<int:topic_id>/', views.add_topic, name='add_topic'),
    # 用于编辑帖子的页面
    path('forum/edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
]