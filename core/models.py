from django.db import models
from django.contrib.auth.models import User #importar para usar a User que já existe no Django
from datetime import datetime, timedelta

# Create your models here.

#nome da minha classe (que irá virar uma tabela no banco de dados)
class Evento(models.Model):
    titulo = models.CharField(max_length=100)  #tipo char com no máximo 100 caracteres
    descricao = models.TextField(blank=True,null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #insere automaticamente a data/hora da criação
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #utilizar aqui a User
    local_evento = models.TextField(blank=True, null=True)

    # para criar a tabela com o nome abaixo e não com o default que o Python cria que será core_evento
    class Meta:
        db_table = 'evento'

    #para exibir o nome do titulo no evento e não evento_object1
    def __str__(self):
        return self.titulo

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d / %m / %Y %H:%M Hrs')

    def get_data_evento(self):
        return self.data_evento.strftime('%d / %m / %Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
