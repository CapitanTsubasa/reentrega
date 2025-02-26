from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, EditUserForm, AvatarForm, UserCreationForm
from .models import Avatar

# Create your views here.
def index(request):
    return render(request, "Main/index.html")

@login_required
def perfil(request):
    return render(request, 'Main/perfil.html', {'user': request.user})

def about(request):
    return render(request, "Main/about.html")

@login_required
# Vista para editar perfil
def editar_perfil(request):
    
    user = request.user  # Usuario autenticado

    avatar_instance = Avatar.objects.filter(user=user).first() #por si se rompe borrar el .first
    
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar_instance)

        if form.is_valid() and avatar_form.is_valid():
            form.save()

            avatar = avatar_form.save(commit=False)
            avatar.user = request.user
            avatar.save()

            return redirect("index")
    else:
        form = EditUserForm(instance=request.user)
        avatar_form = AvatarForm(instance=avatar_instance)

    return render(request, 'Main/editar_perfil.html', {'form': form, 'avatar_form': avatar_form})
    
def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Main/index.html')  # Redirige al perfil tras el registro
    else:
        form = RegistroForm()
    return render(request, 'Main/register.html', {'form': form})

# Vista de Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "Main/login.html", {"error": "Usuario o contraseña incorrectos"})

    return render(request, "Main/login.html")
            
# Vista de Registro
def register_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Main/perfil.html")
    else:
        form = RegistroUsuarioForm()

    return render(request, "Main/register.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # Asegúrate de que 'index' coincide con tu URL en urls.py

def logout_view(request):
    logout(request)
    return redirect("Main:login")  # Redirige al login después de cerrar sesión

@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, "Main/lista_usuarios.html", {"usuarios": usuarios})

def about(request):
    return render(request, "Main/about.html")

def base_view(request):
    return render(request, "Main/base.html")