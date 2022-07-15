from django.urls import path
from . import views

app_name = 'interface'

urlpatterns = [
    path('', views.index, name='index'),
    # 搜索
    path('search/', views.search, name='search'),
    # # 帖子详情页面
    # path('forum/topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    # # 用于添加帖子的页面
    # path('forum/add_topic/', views.add_topic, name='add_ftopic'),
    # path('forum/add_topic/<int:topic_id>/', views.add_topic, name='add_topic'),
    # # 用于编辑帖子的页面
    # path('forum/edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
]