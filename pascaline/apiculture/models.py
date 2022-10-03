from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return f"ID {self.id}. {self.first_name}" #pratique pour la vue web

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=128)
    project_type = models.CharField(max_length=30)
    users = models.ManyToManyField('User', through = 'Contributor')
    
    def __str__(self):
        return f"ID {self.id}. {self.title}"


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    PERM_CHOICES = (
    	('A', 'Author'),
    	('C', 'Contributor'),
    	)
    permission = models.CharField(max_length=1, choices=PERM_CHOICES)
    role = models.CharField(max_length=30)
    
    def __str__(self):
        return f"U{self.user_id}/P{self.project_id}/{self.permission}"
     
    
class Issue(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=128)
    tag = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_created')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_assigned') #deux noms car meme assignement user
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_id}. {self.title}"
        
        
class Comment(models.Model):
    description = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id} (Issue {self.issue_id})"
        