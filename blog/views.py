from django.shortcuts import render
from django.views import generic
from . forms import ContactForm
from .models import Posts


class PostList(generic.ListView):  # views for posts
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4


class PostDetail(generic.DetailView):  # view for each post
    model = Posts
    template_name = 'post.html'


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm
    return render(request, 'contact.html', {'form': form})


