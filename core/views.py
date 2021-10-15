from django.shortcuts import render , redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from datetime import datetime , timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.

def index(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/') #retornar para o index
        else:
            messages.error(request,"Usuário ou senha inválido.")
            return redirect('/')
    else:
        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')

 #só vai permitir abrir a agenda se logar
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1) #data atual menos 1 hora
    evento = Evento.objects.filter(usuario=usuario, #filtrar só do usuário logado
                                   data_evento__gt=data_atual) #__gt para >= e __lt para <= ...filtrar só data atual menos 1 hora
    #evento = Evento.objects.all() #filtrar todos
    dados = {'eventos': evento }
    return render(request,'agenda.html',dados) #chamar a página html

@login_required(login_url='/login/')
#nova def para realizar o cadastro de eventos
def evento(request):
    id_evento = request.GET.get('id') #recuperar o id do evento
    #print(id_evento) #para ver qual o id do evento (aparece na aba run abaixo)
    dados = {} #dicionário vazio
    #se encontrar algum evento..condição do if abaixo
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request,'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        local_evento = request.POST.get('local_evento')
        id_evento = request.POST.get('id_evento')
        #se o id_evento estiver preenchido então realizar a alteração. Caso contrario realizar a criação do novo registro
        if id_evento:
            #existem duas formas de realizar a alteração..a primeira abaixo
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                           data_evento=data_evento,
            #                                           descricao=descricao,
            #                                           local_evento=local_evento)
            #segunda forma de realizar as alterações
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao=descricao
                evento.local_evento=local_evento
                evento.save()
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario,
                                  local_evento=local_evento)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    #Evento.objects.filter(id=id_evento).delete() #aqui tb funciona o delete, mas delete de qualquer usuário. Cada usuário só pode excluir o q é seu
    usuario = request.user
    try: #tratamento para usuários que não existem
      evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    #Só deletar se for do mesmo usuário
    if usuario == evento.usuario:
        evento.delete()
    else: #tratamento para tentativa de exclusão de eventos que não são daquele usuário
        raise Http404()
    return redirect('/')

@login_required(login_url='/login/')
def json_lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id','titulo')
    return JsonResponse(list(evento), safe=False) #tem que converter para lista