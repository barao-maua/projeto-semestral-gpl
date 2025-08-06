from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Acomodacao(models.Model):
    nome = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__ (self):
        return self.nome
    
    

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
    class Generos(models.TextChoices):
        FEMININO = 'Feminino', 'feminino'
        MASCULINO = 'Masculino', 'masculino'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=9, 
                              choices=Generos.choices,
                              default=Generos.FEMININO)


class AvaliacaoUsuario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    acomodacao = models.ForeignKey('Acomodacao', on_delete=models.CASCADE, db_column='id_acomodacao')
    nota =  models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario} para {self.acomodacao}"


class Reserva(models.Model):
    class StatusReserva(models.TextChoices):
        PENDENTE = 'pendente', 'Pendente'
        CONCLUIDA = 'concluida', 'Concluída'
        
    data_inicio = models.DateField()
    data_fim = models.DateField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')
    acomodacao = models.ForeignKey('Acomodacao', on_delete=models.CASCADE, db_column='id_acomodacao')
    status_reserva = models.CharField(
        max_length=10,
        choices=StatusReserva.choices,
        default=StatusReserva.PENDENTE
    )

    def __str__(self):
        return f"Reserva #{self.id} - {self.status_reserva}"

class LogReserva(models.Model):
    class Acoes(models.TextChoices):
        CRIACAO = 'criacao', 'Criação'
        ALTERACAO = 'alteracao', 'Alteração'
        CANCELAMENTO = 'cancelamento', 'Cancelamento'

    acao = models.CharField(  
        max_length=12,
        choices=Acoes.choices,
        default=Acoes.CRIACAO)

    data_hora = models.DateTimeField(auto_now_add=True)
    reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE, db_column='id_reserva')

    def __str__(self):
        return f"Log {self.acao} da Reserva {self.reserva.id}"


class LogUsuario(models.Model):
    class Acoes(models.TextChoices):
        CRIACAO = 'criacao', 'Criação'
        ALTERACAO = 'alteracao', 'Alteração'

    acao = models.CharField(  
        max_length=12,
        choices=Acoes.choices,
        default=Acoes.CRIACAO)

    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='id_usuario')

    def __str__(self):
        return f"Log {self.acao} do Usuário {self.usuario.cpf}"


