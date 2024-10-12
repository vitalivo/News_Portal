from django.urls import path
from .views import post_list, post_detail, category_list, category_posts, news_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/', category_posts, name='category_posts'),
    path('news/', news_list, name='news_list'),  # Новая страница со списком новостей
    path('news/<int:post_id>/', post_detail, name='post_detail'),
]
