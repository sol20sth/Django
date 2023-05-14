from django.urls import path
from . import views

urlpatterns = [
    path("articles/", views.article_list),
    path("<int:article_pk>/", views.article_detail),
    # 타이틀 검색 요청
]
'''
SELECT * 
FROM articles
WHERE title LIKE "%keyword%";
'''
