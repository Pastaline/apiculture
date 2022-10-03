from django.shortcuts import render #legacy
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, ContributorSerializer, ProjectSerializer
from .models import User, Contributor, Project


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']
    

class ContributorViewSet(viewsets.ModelViewSet):
	queryset = Contributor.objects.all()
	serializer_class = ContributorSerializer
	

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post']
    #permission_classes = [IsAuthenticated] ça s'arrête là je n'arrive pas à faire marcher postman
    #mais voilà je pense que la clé est là
    #faire des ModelViewSet tout bête
    # et faire
    # if isAuthenticated(): / if isAuthoroftheProject():
    #		def get(self, *args, **kwargs):
    #		def post(self, *args, **kwargs):
    #		def patch(self, *args, **kwargs):
    #		def delete(self, *args, **kwargs):
    