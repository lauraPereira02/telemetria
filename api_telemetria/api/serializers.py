from rest_framework import serializers
from api_telemetria import models


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da marca'},
            'descricao': {'help_text': 'Descrição da marca'}
        }


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do modelo'},
            'descricao': {'help_text': 'Descrição do modelo'},
            'marcaid': {'help_text': 'Identificador da marca. Buscar no GET da API Marca'}
        }


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da unidade de medida'},
            'descricao': {'help_text': 'Descrição da unidade de medida'},
            'sigla': {'help_text': 'Sigla da unidade de medida'}
        }


class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da medição'},
            'descricao': {'help_text': 'Descrição da medição'},
            'unidademedidaid': {'help_text': 'Identificador da unidade de medida. Buscar no GET da API UnidadeMedida'}
        }


class VeiculoSerializer(serializers.ModelSerializer):
   class Meta:
        model = models.Veiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do veículo'},
            'descricao': {'help_text': 'Descrição do veículo'},
            'ano': {'help_text': 'Ano do veículo'},
            'horimetro': {'help_text': 'Horímetro do veículo'},
            'marcaid': {'help_text': 'Identificador da marca. Buscar no GET da API Marca'},
            'modeloid': {'help_text': 'Identificador do modelo. Buscar no GET da API Modelo'}
        }


class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da Medição veiculo'},
            'veiculoid': {'help_text': 'Identificador do veiculo. Buscar no Get da Api veiculo'},
            'medicaoid': {'help_text': 'Identificador do tipo de medição. Buscar no Get da API Medicao'},
            'data': {'help_text': 'Data e hora da medição realizada'},
            'valor': {'help_text': 'Valor medido'}
        }