from django.urls import path, path
from . import views

app_name = 'books'

urlpatterns = [
    # path自动匹配最长匹配项 repath匹配第一个匹配项

    # 书库的主页，显示标签和一些书籍
    path('', views.index, name='index'),

    # 书籍相关
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/score', views.book_score, name='book_score'), # 评分表单回调页
    path('book/<int:book_id>/<int:chapter_id>/', views.chapter, name='chapter'), # 章节内容页面
    path('add_book/', views.add_book, name='add_book'), # 用于添加书籍的页面
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'), # 用于编辑书籍的页面
    path('add_chapter/<int:book_id>/', views.add_chapter, name='add_chapter'), # 用于添加章节的页面
    path('edit_chapter/<int:book_id>/<int:chapter_id>/', views.edit_chapter, name='edit_chapter'), # 用于编辑章节的页面

    # 系列的详细页面
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),

    # 好句，评论相关
    path('add_gsent/<int:book_id>/', views.add_gsentents, name='add_gsentents'),
    # path('book/<int:book_id>/gsent/<int:gsent_id>', views.) # 好句详细界面
    # path('edit_gsent/<int:book_id>/', views.edit_g_sentence, name='edit_gsent'),
    path('add_comment/<int:book_id>/', views.add_comment, name='add_comment'),

]