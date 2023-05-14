from django.db import models
# 이미지 처리 함수 불러오기
from imagekit.processors import Thumbnail
# 썸네일 전용 이미지 필드
from imagekit.models import ImageSpecField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[Thumbnail(100, 100)],
        format="JPEG",
        options={"quality" : 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'
