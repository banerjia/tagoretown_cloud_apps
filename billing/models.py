from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    created_at = models.DateTimeField(editable=False,auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Customer(models.Model):
    name = models.CharField(max_length=512)
    active = models.BooleanField(default=True)

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    tags = models.CharField(max_length=1024, null=True)
    street_address = models.CharField(max_length=512)
    suite = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=8, default='IN')
    zip_code= models.CharField(max_length=12)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(editable=False,auto_now_add=True)
    comments = GenericRelation(Comment)
