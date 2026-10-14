from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,null=True,blank=True, related_name="tasks"
    )

    def __str__(self):
        return self.title
    
