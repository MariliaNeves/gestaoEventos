from rest_framework import serializers
from gestao.models import Cidade, Evento, Campeonato, ClassificacaoClube, Clube, Fase, Jogo


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class CampeonatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeonato
        fields = '__all__'


class ClassificacaoClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificacaoClube
        fields = '__all__'


class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = '__all__'


class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fase
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'
