"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/',views.lista_eventos), #chamar aqui a nova visão
    path('agenda/lista/', views.json_lista_eventos), #utilizar json
    #path('', views.index) #se for a raiz direcionar para a agenda...pode usar esse ou o abaixo
    path('', RedirectView.as_view(url='/agenda/')), #se for a raiz direcionar para a agenda
    path('agenda/evento/',views.evento),
    path('agenda/evento/submit',views.submit_evento), #nova rota para o botão Salvar
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento), #nova rota para exclusão do evento pela passagem de parametro pelo id_evento
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]
