from django.contrib.auth.models import User, Group
from opacity.api.models import Location, Rating, UserData
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class UserSerializer(serializers.HyperlinkedModelSerializer):
    authentication_classes = [ TokenAuthentication ]
    permission_classes = [ IsAuthenticated, ]
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', "is_staff")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('place_id', 'address', 'ratings', 'id', 'created', 'last_updated')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ('date', 'capacity', 'user', 'location')

class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ('user', 'score', 'id')
