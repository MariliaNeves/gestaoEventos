from rest_framework import viewsets

from gestao.models import Cidade, Evento, Campeonato, ClassificacaoClube, Clube, Fase, Jogo
from gestao.serializer import CidadeSerializer, EventoSerializer, CampeonatoSerializer, ClassificacaoClubeSerializer, \
    ClubeSerializer, FaseSerializer, JogoSerializer


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class CampeonatoViewSet(viewsets.ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer


class ClassificacaoClubeViewSet(viewsets.ModelViewSet):
    queryset = ClassificacaoClube.objects.all()
    serializer_class = ClassificacaoClubeSerializer


class ClubeViewSet(viewsets.ModelViewSet):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer


class FaseViewSet(viewsets.ModelViewSet):
    queryset = Fase.objects.all()
    serializer_class = FaseSerializer


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
