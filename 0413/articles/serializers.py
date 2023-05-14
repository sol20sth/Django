from rest_framework import serializers
from .models import Article


# 1. detail 전용
class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = "__all__"

# 2. list 전용
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ("id", "title", "content")