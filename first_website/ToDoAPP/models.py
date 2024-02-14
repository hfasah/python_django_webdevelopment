from pickle import TRUE
from django.db import models

# Create your models here.
class ToDo_table(models.Model):
    task_name = models.CharField(max_length=255)
    task_date_time = models.TimeField(auto_now=TRUE)
