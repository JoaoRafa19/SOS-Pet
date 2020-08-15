from django.db import models
from django.contrib.auth.models import User #tabela de usuarios default do django

# Create your models here.

class Pet(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    data_criacao = models.DateTimeField(auto_now_add=True) #adiciona automaticamente a data da inscrição
    photo = models.ImageField(upload_to='pet') #adiciona o caminho da imagem ao banco de dados
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # "on_delete=CASCADE" faz com que se um usuario for deletado os pets relacionados a ele também sao deletados

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Pet'
