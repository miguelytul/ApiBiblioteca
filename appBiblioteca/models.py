from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key= True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    senha = models.TextField(max_length=100)
    
    def __str__(self):
        return self.nome