from django.db import models

def articles_image_path(instance, filename):
    return f"images/{filename}"

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()
    # image = models.ImageField(blank=True, upload_to="%Y/%m/%d/")
    image = models.ImageField(blank=True, upload_to=articles_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)