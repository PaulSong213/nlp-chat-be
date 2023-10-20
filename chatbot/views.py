from rest_framework import views
from rest_framework.response import Response
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatbot_init import chatbot_init

chatbot = chatbot_init()


class ChatbotAPI(views.APIView):
    def get(self, request):
        user_message = request.query_params.get('message', '')
        if not user_message:
            return Response({'error': 'Please provide a "message" parameter in the query string.'}, status=status.HTTP_400_BAD_REQUEST)
        statement = Statement(user_message)
        response = chatbot.get_response(statement)  # Pass the statement object
        return Response({'response': str(response)}, status=views.status.HTTP_200_OK)
