from django.db import models
from django.contrib.auth.models import User #importar para usar a User que já existe no Django

# Create your models here.

#nome da minha classe (que irá virar uma tabela no banco de dados)
class Evento(models.Model):
    titulo = models.CharField(max_length=100)  #tipo char com no máximo 100 caracteres
    descricao = models.TextField(blank=True,null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #insere automaticamente a data/hora da criação
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #utilizar aqui a User

    # para criar a tabela com o nome abaixo e não com o default que o Python cria que será core_evento
    class Meta:
        db_table = 'evento'

    #para exibir o nome do titulo no evento e não evento_object1
    def __str__(self):
        return self.titulo
