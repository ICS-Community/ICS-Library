from django.urls import path, path
from . import views

app_name = 'books'

urlpatterns = [
    # path自动匹配最长匹配项 repath匹配第一个匹配项

    # 书库的主页，显示标签和一些书籍
    path('', views.index, name='index'),

    # 书籍的详细页面
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),

    # 系列的详细页面
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),

    # 章节内容页面
    path('book/<int:book_id>/<int:chapter_id>/', views.chapter, name='chapter'),

    # # 搜索页面
    # path('search/', views.search, name='search'),

    # 编辑页面即包含添加，删除
    # 用于编辑章节的页面
    path('edit_chapter/<int:book_id>/<int:chapter_id>/', views.edit_chapter, name='edit_chapter'),

    # # 用于编辑好句的页面
    # path('edit_gsent/<int:book_id>/', views.edit_g_sentence, name='edit_gsent'),

    # 用于编辑标签的页面


]