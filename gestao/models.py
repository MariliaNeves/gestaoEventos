from django.db import models

Flag = (
    ("SIM", "Sim"),
    ("NAO", "Não"),
)

TipoCampeonato = (
    ("ESTADUAL", "ESTADUAL"),
    ("NACIONAL", "NACIONAL"),
    ("INTERNACIONAL", "INTERNACIONAL"),
    ("REGIONAL", "REGIONAL"),
)

Estado = (
    ("AC", "AC"),
    ("AL", "AL"),
    ("AM", "AM"),
    ("AP", "AP"),
    ("BA", "BA"),
    ("DF", "DF"),
    ("ES", "ES"),
    ("GO", "GO"),
    ("MA", "MA"),
    ("MT", "MT"),
    ("MS", "MS"),
    ("MG", "MG"),
    ("PA", "PA"),
    ("PB", "PB"),
    ("PE", "PE"),
    ("PI", "PI"),
    ("PR", "PR"),
    ("RJ", "RJ"),
    ("RN", "RN"),
    ("RO", "RO"),
    ("RR", "RR"),
    ("RS", "RS"),
    ("SC", "SC"),
    ("SE", "SE"),
    ("SP", "SP"),
    ("TO", "TO"),
)


class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=Estado)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, null=True)
    horarioAlterado = models.CharField(max_length=3, choices=Flag)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Campeonato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    urlJson = models.CharField(max_length=300, null=True)
    tipoCampeonato = models.CharField(max_length=20, choices=TipoCampeonato)
    dataInicio = models.DateTimeField(auto_now=False)
    dataFim = models.DateTimeField(auto_now=False)
    localizacao = models.CharField(max_length=50, null=True)
    numeroRodadaAtual = models.IntegerField(null=True)
    apagado = models.CharField(max_length=3, choices=Flag)
    peso = models.FloatField(null=True)
    campeonatoSlug = models.CharField(max_length=50, null=True)
    edicaoSlug = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nome


class ClassificacaoClube(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Clube(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    slug = models.CharField(max_length=50, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    classificacaoClube = models.ForeignKey(ClassificacaoClube, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Fase(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)
    peso = models.FloatField(null=True)
    dataInicio = models.DateTimeField(auto_now=False)
    dataFim = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    mandante = models.ForeignKey(Clube, related_name='mandante', on_delete=models.PROTECT)
    visitante = models.ForeignKey(Clube, related_name='visitante', on_delete=models.PROTECT)
    rodada = models.IntegerField(null=True)
    fase = models.ForeignKey(Fase, on_delete=models.PROTECT)
    estado = models.CharField(max_length=3, choices=Estado)
    classificacaoJogo = models.CharField(max_length=100)
    idSde = models.IntegerField(null=True)

    def __str__(self):
        return self.nome
