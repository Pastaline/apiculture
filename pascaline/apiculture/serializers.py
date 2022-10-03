from rest_framework import serializers

from .models import User, Contributor, Project


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password']
				

class ContributorSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user_id')
	project = serializers.ReadOnlyField(source='project_id')
	class Meta:
		model = Contributor
		fields = ['user', 'project', 'permission', 'role']
		

class ProjectSerializer(serializers.ModelSerializer):
	pk = serializers.SerializerMethodField()
	
	#ct = Contributor.objects.prefetch_related()
	#contributors = ContributorSerializer(ct, many=True)
	#for contributor in contributors.data:
	#	print("------>", contributor)
	#possible optimisation s'il y a bcp d'entrées dans Contributor
		
	class Meta:
		model = Project
		fields = ['pk', 'title', 'description', 'project_type']
		
	def get_pk(self, instance):
		return instance.pk #à utiliser pour ajouter l'auteur dans Contributor?
		