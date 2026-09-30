from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("TODO","To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE","Done"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="TODO")
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
