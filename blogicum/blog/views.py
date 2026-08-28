from django.conf import settings
from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def index(request):
    post_list = Post.published.for_index_page().select_related(
        'author', 'category', 'location'
    )[:settings.POSTS_PER_PAGE_LIMIT]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(
        Post.published.published().select_related(
            'author', 'category', 'location'
        ),
        pk=pk
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.published.published(),
        slug=category_slug,
    )
    post_list = category.category_posts.published().select_related(
        'author', 'location'
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
