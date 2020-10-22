from django.shortcuts import render
from .serializers import Profile_Serializers
from rest_framework import viewsets,permissions
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView
from .models import Profile_Model

class Profilecreate_view(CreateAPIView):
    # permission_classes=[permissions.IsAuthenticated]
    queryset=Profile_Model.objects.all()
    serializer_class= Profile_Serializers

class ProfileRetrive_view(RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated]
    lookup_field='id'
    queryset=Profile_Model.objects.all()
    serializer_class=Profile_Serializers

class Profileupdate_view(UpdateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=Profile_Serializers
    lookup_field='id'
    queryset=Profile_Model.objects.all()
