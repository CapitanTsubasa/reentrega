from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


def post_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        post_list = Post.objects.filter(titulo__icontains=busqueda)
    else:
        post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': post_list})

class PostListView(ListView):
    model = Post
    template_name = "blog:post_list.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect('blog:post_list')
            else:
                form.add_error(None, "Debes estar logueado para crear una publicacion.")
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', context={'form': form})

class PostDetailView(DetailView):
    model = Post
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    
