from django.urls import path, include
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
    path("<int:pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("comments/<int:pk>/", views.CommentDetailAPIView.as_view(), name="comment_detail"),
]   