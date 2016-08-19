from rest_framework import serializers
from lugares.models import Local, Atributo, Review


class LocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Local
        fields = ('id', 'nome', 'dono', 'endereco', 'bairro', 'cidade', 'estado', 'pais', 'atributos')
        depth = 1


class AtributoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atributo
        fields = ('id', 'nome',)
        depth = 0


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'local', 'titulo', 'texto', 'avaliacao', 'autor')
        depth = 1
