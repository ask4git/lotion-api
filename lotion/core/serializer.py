from rest_framework import serializers as s
from lotion.core import models as m


class DocumentSerializer(s.ModelSerializer):
    class Meta:
        model = m.Document
        fields = ['uid', 'title']
