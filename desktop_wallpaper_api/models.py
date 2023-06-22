from django.db import models

# Create your models here.

class Wallpaper(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.URLField(max_length=300)

    def __str__(self):
        return self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "imageURL": self.imageURL
        }
    
    