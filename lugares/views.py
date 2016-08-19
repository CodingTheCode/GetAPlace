# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lugares.models import Local
from lugares.serializers import LocalSerializer

cabecalhos = {'Access-Control-Allow-Origin': '*', }


@csrf_exempt
@api_view(['GET'])
def lugares_list(request):

    locais = Local.objects.all()[:30]
    serializer = LocalSerializer(locais, many=True)
    return Response(serializer.data, headers=cabecalhos)

@csrf_exempt
@api_view(['GET'])
def lugares_busca(request, nome_busca):
    import pdb; pdb.set_trace()
    locais =Local.objects.filter(nome=nome_busca)
    serializer = LocalSerializer(locais, many=True)
    return Response(serializer.data, headers=cabecalhos)
