from django.db import models
from shortid import ShortId

SID_GENERATOR = ShortId()


def generate_sid():
    return str(SID_GENERATOR.generate())


class Document(models.Model):
    uid = models.CharField(primary_key=True, max_length=24, editable=False, default=generate_sid)
    parent_uid = models.CharField(max_length=255, null=True, blank=True, default="ROOT")
    child_uid = models.JSONField(default=list, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now_add=True, editable=True)
    is_activate = models.BooleanField(default=True)
