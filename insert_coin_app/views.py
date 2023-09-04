
from django.shortcuts import render, redirect
from insert_coin_app.models import *
from django.http import HttpResponse
from .models import Socios, XBOX_series_x, Avatar
from .forms import SociosForm, RegistroUsuariosForm, UserEditForm, AvatarForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "insert_coin_app/home.html")

def ps5(request):
    contexto = {'PS5': PS5.objects.all(), 'titulo': 'Listado de juegos de Playstation 5'}
    return render(request, "insert_coin_app/ps5.html", contexto)

@login_required
def xbox(request):
    contexto = {'XBOX': XBOX_series_x.objects.all()}
    return render(request, "insert_coin_app/xbox.html", contexto)

def otras_consolas(request):
    return render(request, "insert_coin_app/otras_consolas.html")

def socios(request):
    contexto = {'Socios': Socios.objects.all()}
    return render(request, "insert_coin_app/socios.html", contexto)


def about_me(request):
    return render(request, "insert_coin_app/about_me.html")

@login_required
def sociosform(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST.get('email')
        edad = request.POST['edad']
        
        socios = Socios(nombre=nombre, apellido=apellido, email=email, edad=edad)
        socios.save()
        
        return render(request, "insert_coin_app/nuevo_socio.html")
    
    return render(request, "insert_coin_app/sociosForm.html")

@login_required
def sociosform2(request):
    if request.method == "POST":
        miForm= SociosForm(request.POST)
        if miForm.is_valid():
            socios_nombre= miForm.cleaned_data.get('nombre')
            socios_apellido = miForm.cleaned_data.get('apellido')
            socios_email = miForm.cleaned_data.get('email')
            socios_edad = miForm.cleaned_data.get('edad')
            socios = Socios(nombre=socios_nombre,
                            apellido=socios_apellido,
                            email = socios_email,
                            edad = socios_edad) 
            socios.save()
            return render(request, "insert_coin_app/base.html")
    else:
        miForm = SociosForm()

    return render(request, "insert_coin_app/sociosForm2.html", {"form" : miForm})


def buscar_juegos(request):
    return render(request, "insert_coin_app/buscar_juegos.html")


def buscar_juegos2(request):
    if request.GET['buscar_juegos']:
       patron = request.GET['buscar_juegos']
       ps5 = PS5.objects.filter(nombre__icontains = patron)
       contexto = {'PS5': ps5}
       return render(request, "insert_coin_app/ps5.html", contexto)
    return render(request, "insert_coin_app/buscar_juegos2.html")


@login_required
def updateXbox(request, id_xbox):
    xbox = XBOX_series_x.objects.get(id=id_xbox)
    if request.method == 'POST':
        miForm = XBOXForm(request.POST)
        if miForm.is_valid():
            xbox.nombre = miForm.cleaned_data.get('nombre')
            xbox.genero = miForm.cleaned_data.get('genero')
            xbox.online = miForm.cleaned_data.get('online')
            xbox.precio = miForm.cleaned_data.get('precio')
            xbox.save()
            return redirect(reverse_lazy('xbox'))
    else: 
        miForm = XBOXForm(initial={
            'nombre': xbox.nombre,
            'genero': xbox.genero,
            'online': xbox.online,
            'precio': xbox.precio,
        })
        return render(request, "insert_coin_app/xboxForm.html", {'form':miForm})

@login_required    
def deleteXbox(request, id_xbox):
    xbox = XBOX_series_x.objects.get(id=id_xbox)
    xbox.delete()
    return redirect(reverse_lazy('xbox'))

@login_required
def createXbox(request):
    if request.method == 'POST':
        miForm = XBOXForm(request.POST)
        if miForm.is_valid():
            x_nombre = miForm.cleaned_data.get('nombre')
            x_genero = miForm.cleaned_data.get('genero')
            x_online = miForm.cleaned_data.get('online')
            x_precio = miForm.cleaned_data.get('precio')
            xbox = XBOX_series_x(nombre = x_nombre,
                                 genero = x_genero,
                                 online = x_online,
                                 precio = x_precio
                                 )
            xbox.save()
            return redirect(reverse_lazy('xbox'))
    else: 
        miForm = XBOXForm()
    return render(request, "insert_coin_app/xboxForm.html", {'form':miForm})




class Otras_consolas_List(LoginRequiredMixin, ListView):
    model = Otras_consolas

class Otras_consolas_create(LoginRequiredMixin, CreateView):
    model = Otras_consolas
    fields = ('nombre', 'plataforma', 'genero', 'online', 'precio')
    success_url = reverse_lazy('otras_consolas')

class Otras_consolas_update(LoginRequiredMixin, UpdateView):
    model = Otras_consolas
    fields = ('nombre', 'plataforma', 'genero', 'online', 'precio')
    success_url = reverse_lazy('otras_consolas')

class Otras_consolas_delete(LoginRequiredMixin, DeleteView):
    model = Otras_consolas
    success_url = reverse_lazy('otras_consolas')



def login_request(request):
    if request.method == 'POST':
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data['username']
            password = miForm.cleaned_data['password']
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar ="/media/avatares/default.png"
                finally: 
                    request.session["avatar"] = avatar
                return render(request, "insert_coin_app/home.html", {"mensaje" :"Bienvenido a nuestra tienda online INSERT COINS"})
            else: 
                return render(request, "insert_coin_app/login.html", {'form':miForm, "mensaje" : f"El usario o password que ha ingresado no son válidos " })
    
        else: 
            return render(request, "insert_coin_app/login.html", {'form':miForm, "mensaje" : f"El usario o password que ha ingresado no son válidos " })
    miForm = AuthenticationForm()

    return render(request, "insert_coin_app/login.html", {'form':miForm})


def register(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "insert_coin_app/home.html")
    else: 
        miForm = RegistroUsuariosForm()

    return render(request, "insert_coin_app/registro.html", {'form':miForm})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get ('email')
            usuario.name = form.cleaned_data.get ('name')
            usuario.last_name = form.cleaned_data.get ('last_name')
            usuario.password1 = form.cleaned_data.get ('password1')
            usuario.password2 = form.cleaned_data.get ('password2')
            usuario.save()
            return render (request, "Insert_coin_app/home.html")
        else:
            return render (request, "Insert_coin_app/editarPerfil.html", { 'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render (request, "Insert_coin_app/editarPerfil.html", { 'form': form, 'usuario': usuario.username}) 


@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render (request, "Insert_coin_app/home.html")
    else:
        form = AvatarForm()
    return render (request, "Insert_coin_app/agregar_avatar.html", {'form': form})
        
#Ps5

class PS5_List(LoginRequiredMixin, ListView):
    model = PS5

class PS5_create(LoginRequiredMixin, CreateView):
    model = PS5
    fields = ('nombre','genero', 'online', 'precio')
    success_url = reverse_lazy('ps5')

class PS5_update(LoginRequiredMixin, UpdateView):
    model = PS5
    fields = ('nombre','genero', 'online', 'precio')
    success_url = reverse_lazy('ps5')

class PS5_delete(LoginRequiredMixin, DeleteView):
    model = PS5
    success_url = reverse_lazy('ps5')


