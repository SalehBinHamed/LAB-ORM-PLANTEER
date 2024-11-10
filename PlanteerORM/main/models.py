from django.db import models

# Create your models here.
class Clint(models.Model):
    first_name = models.CharField(max_length=2048)
    last_name = models.CharField(max_length=2048)
    email = models.EmailField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)