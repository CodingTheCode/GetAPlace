# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lugares.models import Local, Review, Atributo
from lugares.serializers import LocalSerializer, ReviewSerializer
from django.views.generic.base import TemplateView

import json


class OnePageAppView(TemplateView):
    template_name = 'index.html'


@csrf_exempt
@api_view(['GET', 'POST'])
def lugares(request):

    if(request.method == 'GET'):
        locais = Local.objects.all()[:30]
        serializer = LocalSerializer(locais, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif(request.method == 'POST'):
        data = json.loads(request.body)
        dono_atual = User.objects.get(id=data['dono'])
        novo_local = Local.objects.create(dono=dono_atual, nome=data['nome'], endereco=data['endereco'], bairro=data['bairro'], cidade=data['cidade'], estado=data['estado'], pais=data['pais'])

        # Atributos
        for atr in data['atributos']:
            novo_local.atributos.add(Atributo.objects.get(nome=atr['nome']))

        serializer = LocalSerializer(novo_local)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def lugar(request, id):

    local = Local.objects.get(id=id)
    serializer = LocalSerializer(local)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Retorna todos os reviews de um local baseado em seu id
@csrf_exempt
@api_view(['GET'])
def reviews_lugar(request, id):
    reviews = Local.objects.get(id=id).reviews
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#cria uma nova locação
@csrf_exempt
@api_view(['POST'])
def locacao_criar(request):
    local_locacao = Local.objects.get(id=request.data['local'])
    locatario = User.objects.get(id=request.data['locatario'])
    diaLocacao = request.data['dataDaLocacao']
    valor = request.data['valor']
    novaLocacao = Review.objects.create(local=local_locacao, locatario=locatario,
        dataDaLocacao=dataDaLocacao, valor=valor)
    serializer = ReviewSerializer(novaLocacao)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Cria uma nova review
@csrf_exempt
@api_view(['POST'])
def reviews_criar(request):
    local_atual = Local.objects.get(id=request.data['local'])
    autor_atual = User.objects.get(id=request.data['autor'])
    nova_review = Review.objects.create(local=local_atual, titulo=request.data['titulo'], texto=request.data['texto'], avaliacao=request.data['avaliacao'], autor=autor_atual)
    serializer = ReviewSerializer(nova_review)
    return Response(serializer.data, status=status.HTTP_200_OK)

#busca um registro de locação baseado em parâmetros
@csrf_exempt
@api_view(['GET'])
def locacao_busca(request, locacao_nome_busca, locacao_bairro_busca,locacao_tags_busca):
    locacoes =  Locacao.objects.all()

    if(locacao_nome_busca !="_"):
        locacoesTemp = Locacao.objects.filter(locacao__nome__istartswith=locacao_nome_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(locacao_bairro_busca !="_"):
        locacoesTemp = Locacao.objects.filter(locacao__bairro__istartswith=locacao_bairro_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(locacao_tags_busca != "_"):
        listaTags = tags_busca.split(",")
        for tag in listaTags:
            locaisTemp = Locacao.objects.filter(atributos__nome__istartswith=tag)
            locais = list(set(locais) & set(locaisTemp))


#busca registos de locais baseado e todos os campos de busca
@csrf_exempt
@api_view(['GET'])
def lugares_busca(request, nome_busca, endereco_busca, bairro_busca, cidade_busca,
    estado_busca, pais_busca, tags_busca):

    locais = Local.objects.all()

    if(nome_busca != "_"):
        locaisTemp = Local.objects.filter(nome__istartswith=nome_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(endereco_busca != "_"):
        locaisTemp = Local.objects.filter(endereco__istartswith=endereco_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(bairro_busca != "_"):
        locaisTemp = Local.objects.filter(bairro__istartswith=bairro_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(cidade_busca != "_"):
        locaisTemp = Local.objects.filter(cidade__istartswith=cidade_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(estado_busca != "_"):
        locaisTemp = Local.objects.filter(estado__istartswith=estado_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(pais_busca != "_"):
        locaisTemp = Local.objects.filter(pais__istartswith=pais_busca)
        locais = list(set(locais) & set(locaisTemp))

    if(tags_busca != "_"):
        listaTags = tags_busca.split(",")
        for tag in listaTags:
            locaisTemp = Local.objects.filter(atributos__nome__istartswith=tag)
            locais = list(set(locais) & set(locaisTemp))

    serializer = LocalSerializer(locais, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
