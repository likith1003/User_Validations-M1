from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=50)
    spno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cls = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)

    def __str__(self):
        return self.sname