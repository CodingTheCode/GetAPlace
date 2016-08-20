# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lugares.models import Local
from lugares.serializers import LocalSerializer


@csrf_exempt
@api_view(['GET'])
def lugares_list(request):

    locais = Local.objects.all()[:30]
    serializer = LocalSerializer(locais, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
