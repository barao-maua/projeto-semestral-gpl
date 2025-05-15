from django.db import models
from django.contrib.auth.models import User

class Acomodacao(models.Model):
    nome = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__ (self):
        return self.nome
    
    def __str__ (self):
        return self.capacidade
    
    def __str__ (self):
        return self.descricao
    

class AcomodacaoImagem(models.Model):
    acomodacao = models.ForeignKey(Acomodacao, on_delete=models.CASCADE)
    imagem_url = models.CharField(max_length=255)
    ordem = models.IntegerField(default=1)

    def __str__ (self):
        return self.imagem_url

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero_casa = models.IntegerField()
    observacao = models.CharField(max_length=100)

class Usuario(models.Model):
    GENEROS = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=1, choices=GENEROS)


class AvaliacaoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    acomodacao = models.ForeignKey('Acomodacao', on_delete=models.CASCADE, db_column='id_acomodacao')
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario} para {self.acomodacao}"


class Reserva(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    ]

    id = models.AutoField(primary_key=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    acomodacao = models.ForeignKey('Acomodacao', on_delete=models.CASCADE, db_column='id_acomodacao')
    statusReserva = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Reserva #{self.id} - {self.statusReserva}"


class LogReserva(models.Model):
    ACAO_CHOICES = [
        ('criacao', 'Criação'),
        ('alteracao', 'Alteração'),
        ('cancelamento', 'Cancelamento'),
    ]

    id = models.AutoField(primary_key=True)
    acao = models.CharField(max_length=12, choices=ACAO_CHOICES)
    data_hora = models.DateTimeField(auto_now_add=True)
    reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE, db_column='id_reserva')

    def __str__(self):
        return f"Log {self.acao} da Reserva {self.reserva.id}"


class LogUsuario(models.Model):
    ACAO_CHOICES = [
        ('criacao', 'Criação'),
        ('alteracao', 'Alteração'),
    ]

    id = models.AutoField(primary_key=True)
    acao = models.CharField(max_length=10, choices=ACAO_CHOICES)
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')

    def __str__(self):
        return f"Log {self.acao} do Usuário {self.usuario.cpf}"


