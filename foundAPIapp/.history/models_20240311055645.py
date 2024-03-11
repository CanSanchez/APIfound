from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name