from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

STATUS = [
    ('Publish', 'Publish'),
    ('Unpublish', 'Unpublish'),
]

CATEGORY = [
    ('High Priority', 'High Priority'),
    ('Low Priority', 'Low Priority'),
]


# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="title", max_length=255)
    description = models.TextField(verbose_name="description")
    category = models.CharField(verbose_name="category", max_length=255, choices=CATEGORY, null=True, blank=True)
    due_date = models.DateTimeField(verbose_name="due_date", default=datetime.now)
    is_active = models.BooleanField(verbose_name="is_active", default=False)
    status = models.CharField(verbose_name="status", max_length=255, choices=STATUS, null=True, blank=True)
    owner = models.ForeignKey(User, verbose_name="owner", related_name="owner", on_delete=models.CASCADE)
    changed_by = models.IntegerField(verbose_name="changed_by", default=0)
    created_at = models.DateTimeField(verbose_name="created_at", default=datetime.now)
    updated_at = models.DateTimeField(verbose_name="updated_at", default=datetime.now)


    def __str__(self):
        if self.title:
            return self.title
        else:
            return "No Todo title"
