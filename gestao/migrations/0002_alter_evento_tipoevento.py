# Generated by Django 3.2.6 on 2022-02-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tipoEvento',
            field=models.CharField(choices=[('JOGO', 'Jogo'), ('LUTA', 'Luta')], max_length=15),
        ),
    ]
