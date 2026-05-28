from django.db import models
# Importa o sistema de models do Django


# Criação da tabela Usuario
class Usuario(models.Model):

    # Campo ID automático
    # primary_key=True define esse campo como chave primária
    id_usuario = models.AutoField(primary_key=True)

    # Campo de texto para armazenar o nome
    nome = models.TextField(max_length=255)

    # Campo de texto para armazenar email
    email = models.TextField(max_length=255)

    # Campo de texto para armazenar senha
    senha = models.TextField(max_length=100)

    
    # Define como o objeto será exibido no painel admin
    # ou em prints do Python
    def __str__(self):

        # Retorna o nome do usuário
        return self.nome