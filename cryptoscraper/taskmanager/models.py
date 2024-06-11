import uuid
from django.db import models

# Create your models here.

class Job(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, default='pending')

class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    coin = models.CharField(max_length=10)
    data = models.JSONField()
    status = models.CharField(max_length=20, default='pending')
