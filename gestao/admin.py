from django.contrib import admin

from gestao.models import Cidade, Evento, Campeonato, ClassificacaoClube, Clube, Fase, Jogo

admin.site.register(Cidade)
admin.site.register(Evento)
admin.site.register(Campeonato)
admin.site.register(ClassificacaoClube)
admin.site.register(Clube)
admin.site.register(Fase)
admin.site.register(Jogo)
