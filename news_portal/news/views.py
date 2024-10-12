from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def news_list(request):
    posts = Post.objects.filter(post_type='news').order_by('-created_at')  # Фильтрация по типу 'новости'
    return render(request, 'news/news_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'news/post_detail.html', {'post': post})



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'news/post_list.html', {'posts': posts})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'news/category_list.html', {'categories': categories})

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, 'news/category_posts.html', {'category': category, 'posts': posts})

