from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name="home"),
    
    path('xbox/', xbox, name="xbox"),
    path('socios/', socios, name="socios"),
    
    
    path('about_me/', about_me, name="about_me"),
    
    path('sociosForm/', sociosform, name="socios_form"),
    path('sociosForm2/', sociosform2, name="socios_form2"),
    
    path('buscar_juegos/', buscar_juegos, name="buscar_juegos"),
    path('buscar_juegos2/', buscar_juegos2, name="buscar_juegos2"),
   
    path('update_xbox/<id_xbox>', updateXbox, name="update_xbox"),
    path('delete_xbox/<id_xbox>', deleteXbox, name="delete_xbox"),
    path('create_xbox/', createXbox, name="create_xbox"),

    path('update_otras_consolas/<int:pk>', Otras_consolas_update.as_view(), name="update_otras_consolas"),
    path('delete_otras_consolas/<int:pk>', Otras_consolas_delete.as_view(), name="delete_otras_consolas"),
    path('create_otras_consolas/', Otras_consolas_create.as_view(), name="create_otras_consolas"),

    path('otras_consolas/', Otras_consolas_List.as_view(), name="otras_consolas"),

    path('update_ps5/<int:pk>', PS5_update.as_view(), name="update_ps5"),
    path('delete_ps5/<int:pk>', PS5_delete.as_view(), name="delete_ps5"),
    path('create_ps5/', PS5_create.as_view(), name="create_ps5"),

    path('ps5/', PS5_List.as_view(), name="ps5"),

    
    

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="insert_coin_app/logout.html"), name="logout"),
    path('registro/', register, name="registro"), 
    path('editarPerfil/', editarPerfil, name="editar_perfil"),

    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


    ]