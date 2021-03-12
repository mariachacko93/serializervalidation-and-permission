from django.shortcuts import render

# Create your views here.
from validation.models import comment
from rest_framework import serializers,viewsets
from validation.serializers import commentserializer



class commentView(viewsets.ModelViewSet):
    queryset=comment.objects.all()
    serializer_class=commentserializer
