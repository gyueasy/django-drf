from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .bots import translate_bot, analyze_conversation

def chat_view(request):
    return render(request, 'chat.html')

class TranslateAPIView(APIView):

    def post(self, request):
        data = request.data
        message = data.get("message", "")
        translated_message = translate_bot(message)
        return Response({"translated_message": translated_message})
    
class ConversationAnalysisAPIView(APIView):
    def post(self, request):
        data = request.data
        conversation = data.get("conversation", "")
        
        # 대화 분석 요청
        analysis_result = analyze_conversation(conversation)
        
        # 분석 결과 반환
        if 'error' in analysis_result:
            return Response({"error": analysis_result['error']}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(analysis_result, status=status.HTTP_200_OK)