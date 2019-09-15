from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    template_name = 'posts/lista.html'
    model = Post
    context_object_name = 'Posts'


class PostDetailView(DetailView):
    template_name = 'posts/detalhe.html'
    model = Post
    context_object_name = 'Post'
