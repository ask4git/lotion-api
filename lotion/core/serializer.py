from rest_framework import serializers as s
from lotion.core import models as m


class DocumentSerializer(s.ModelSerializer):
    class Meta:
        model = m.Document
        fields = ['content', 'title', 'parent_uid']


class DocumentInactivateSerializer(s.ModelSerializer):
    class Meta:
        model = m.Document
        fields = ['is_activate']


class ReadDocumentSerializer(s.ModelSerializer):
    class Meta:
        model = m.Document
        fields = '__all__'
