from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models as models
from django.contrib.auth.models import User, Group
from django.utils.dateformat import format
from datetime import datetime
import uuid

# Create your models here.
class Location(models.Model):
    address = models.TextField(max_length=500)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    place_id = models.CharField(max_length=255)

    # Relationship Fields
    ratings = models.ManyToManyField('api.Rating', related_name="rates", blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.id

class Rating(models.Model):

    # Fields
    date = models.DateTimeField(auto_now_add=True, editable=False)
    capacity = models.PositiveIntegerField()

    # Relationship Fields
    user = models.ForeignKey(User, )
    location = models.ForeignKey('api.Location', blank=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.id

class UserData(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    score = models.PositiveIntegerField()

    # Relationship Fields
    user = models.OneToOneField(User, )
    ratings = models.ManyToManyField('api.Rating', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.user.name


