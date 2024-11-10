from django.db import models


class Plant(models.Model):
    class CategoryChoices(models.TextChoices):  
        FLOWER = 'flower', 'Flower'
        TREE = 'tree', 'Tree'
        HERB = 'herb', 'Herb'
        SUCCULENT = 'succulent', 'Succulent'

    name = models.CharField(max_length=2048)
    about= models.TextField()
    used_for= models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(
        max_length=2048, 
        choices=CategoryChoices.choices
    )    
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
