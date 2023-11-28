from django.shortcuts import render

from .models import Posts
from django.views import generic


class PostList(generic.ListView):  # views for posts
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4


class PostDetail(generic.DetailView):  # view for each post
    model = Posts
    template_name = 'post.html'


def home(request):
    return render(request, 'home.html', {})

