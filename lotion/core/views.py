from django.shortcuts import render
from rest_framework import permissions as p
from lotion.core import models as m
from lotion.core import serializer as s
from rest_framework.generics import ListCreateAPIView


class DocumentListCreateView(ListCreateAPIView):
    queryset = m.Document.objects
    serializer_class = s.DocumentSerializer
    permission_classes = []