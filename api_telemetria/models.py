from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    descricao = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='veiculos')
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='veiculos')
    ano = models.IntegerField()
    horimetro = models.IntegerField()

    def __str__(self):
        return self.descricao


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Medicao(models.Model):
    TIPO_CHOICES = [
        ('combustivel', 'Combustível'),
        ('manutencao', 'Manutenção'),
        ('outro', 'Outro'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE, related_name='medicoes')

    def __str__(self):
        return self.tipo


class MedicaoVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='medicoes')
    medicao = models.ForeignKey(Medicao, on_delete=models.CASCADE, related_name='veiculos')
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.veiculo} - {self.medicao} - {self.data}"
