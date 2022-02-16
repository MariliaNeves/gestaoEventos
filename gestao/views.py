from rest_framework import viewsets

from gestao.models import Cidade
from gestao.serializer import CidadeSerializer


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
