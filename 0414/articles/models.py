from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    

"""
SELECT *
FROM articles
WHERE title LIKE '%keyword%' AND content LIKE '%keyword%'

SELECT *
FROM articles
WHERE pk >= 30 AND content LIKE '%to%'
"""