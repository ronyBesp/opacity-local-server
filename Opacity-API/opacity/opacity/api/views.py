from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from opacity.api.serializers import UserSerializer, GroupSerializer, LocationSerializer, RatingSerializer, UserDataSerializer
from opacity.api.models import Location, Rating, UserData
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework import permissions, mixins
from django.shortcuts import get_object_or_404

class UserViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    #queryset = User.objects.all() #.order_by('-date_joined')
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.user
        queryset = queryset.filter(username=user)
        return queryset

    def get_object(self):
        if self.request.user.is_staff:
            return super(UserViewSet, self).get_object()
        else:
            return self.request.user

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LocationViewSet(viewsets.ModelViewSet):
    #queryset = Location.objects.all()    
    serializer_class = LocationSerializer
    def get_queryset(self):
        queryset = Location.objects.all()
        print(self.request.query_params)
        place_id = self.request.query_params.get('place_id', None)
        if place_id is not None:
            queryset = queryset.filter(place_id=place_id)
            print(len(queryset))
            print(place_id)
        return queryset

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class UserDataViewSet(viewsets.ModelViewSet):
    #queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    
    def get_queryset(self):
        queryset = UserData.objects.all()
        print(self.request.query_params)
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    callback_url = "127.0.0.1:8081"
    client_class = OAuth2Client
