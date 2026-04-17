from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from men.models import Men


def men_home(request):
    posts = Men.objects.all()
    return render(request, 'men/index.html', {'posts': posts})


def show_post(request, post_slug):
    post = get_object_or_404(Men, slug=post_slug)
    return render(request, 'men/post.html', {'post': post})




