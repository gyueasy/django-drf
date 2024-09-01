from django.urls import path
from . import views
from .views import chat_view

urlpatterns = [
    path("translate/", views.TranslateAPIView.as_view(), name="translate"),
    path('chat/', chat_view, name='chat'),
]