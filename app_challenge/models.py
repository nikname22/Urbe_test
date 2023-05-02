from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    projeto = models.TextField(max_length=255)
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    tir_media = models.IntegerField(null=True)
    total_captado = models.IntegerField(null=True)
    vgv = models.IntegerField(null=True)

    