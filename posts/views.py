from django.urls import reverse_lazy

from .models import Post
from .forms import SalvaPostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime


class PostListView(ListView):
    template_name = 'posts/lista.html'
    model = Post
    context_object_name = 'Posts'


class PostDetailView(DetailView):
    template_name = 'posts/detalhe.html'
    model = Post
    context_object_name = 'Post'


class PostCreateView(CreateView):
    template_name = 'posts/novo.html'
    model = Post
    form_class = SalvaPostForm
    success_url = reverse_lazy('posts:lista')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
    template_name = 'posts/edita.html'
    model = Post
    fields = [
        'titulo',
        'sub_titulo',
        'thumb',
        'descricao',
        'slug',
        'tags',
    ]
    success_url = reverse_lazy('posts:lista')

    def form_valid(self, form):
        form.instance.data_atualizacao = datetime.now()
        return super(PostUpdateView, self).form_valid(form)


class PostDeleteView(DeleteView):
    template_name = 'posts/exclui.html'
    model = Post
    context_object_name = 'Post'
    success_url = reverse_lazy('posts:lista')
