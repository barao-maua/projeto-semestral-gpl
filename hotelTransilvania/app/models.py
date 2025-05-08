from django.db import models

class Acomodacao(models.Model):
    nome = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__ (self):
        return self.nome

    class Meta():
        db_table = 'acomodacao'
        managed = False