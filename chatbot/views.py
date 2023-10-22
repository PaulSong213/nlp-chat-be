from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Import AllowAny from rest_framework.permissions
from rest_framework.permissions import AllowAny
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatbot_init import chatbot_init

chatbot = chatbot_init()


class ChatbotAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_message = request.query_params.get('message', '')
        if not user_message:
            return Response({'error': 'Please provide a "message" parameter in the query string.'}, status=status.HTTP_400_BAD_REQUEST)
        statement = Statement(user_message)
        response = chatbot.get_response(statement)
        return Response({'response': str(response)}, status=status.HTTP_200_OK)
