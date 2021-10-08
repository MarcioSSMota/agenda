from django.contrib import admin
from core.models import Evento #importar a nova classe eventos criada no models.py

# Register your models here.

#exibir mais
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento')
    list_filter = ('usuario', 'titulo',) #virgula tem q estar no final

#registrar a nova classe eventos criada no models.py
admin.site.register(Evento , EventoAdmin) #associar também a nova EventoAdmin