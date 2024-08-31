from django.urls import path
from . import views
from .views import chat_view, ConversationAnalysisAPIView

urlpatterns = [
    path("translate/", views.TranslateAPIView.as_view(), name="translate"),
    path('analyze/', ConversationAnalysisAPIView.as_view(), name='analyze'),
    path('chat/', chat_view, name='chat'),
]