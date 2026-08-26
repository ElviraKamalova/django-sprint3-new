from django.conf import settings
from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def index(request):
    template = 'blog/index.html'
    post_list = Post.published.for_index_page()[:settings.POSTS_PER_PAGE_LIMIT]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.published.published(),
        pk=id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.published.published(),
        slug=category_slug,
    )
    post_list = Post.published.published().filter(
        category_id=category.id
    ).select_related('category', 'location')
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
