from rest_framework import permissions as p
from lotion.core import models as m
from lotion.core import serializer as s
from drf_rw_serializers.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)


class DocumentListCreateView(ListCreateAPIView):
    queryset = m.Document.objects.filter(is_activate=True)
    read_serializer_class = s.ReadDocumentSerializer
    write_serializer_class = s.DocumentSerializer
    permission_classes = []


class DocumentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = m.Document.objects.filter(is_activate=True)
    read_serializer_class = s.ReadDocumentSerializer
    write_serializer_class = s.DocumentSerializer
    permission_classes = []
    lookup_field = 'uid'


class DocumentInactivateUpdateAPIView(UpdateAPIView):
    queryset = m.Document.objects.all()
    read_serializer_class = s.ReadDocumentSerializer
    write_serializer_class = s.DocumentInactivateSerializer
    permission_classes = []
    lookup_field = 'uid'
