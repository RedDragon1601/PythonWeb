from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 16)
    body = models.TextField()
    image = models.ImageField(null = True)

    def __str__(self):
        return self.title