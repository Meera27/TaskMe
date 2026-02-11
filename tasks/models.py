from django.db import models

# Create your models here.
class Task(models.Model):
    status_available = [
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ]
    
    title = models.CharField(max_length=45)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=status_available)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title