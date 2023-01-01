from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from intentMessages.models import IntentMessages
from intentMessages.serializers import IntentMessagesSerializer
from information import views

class ListIntentMessages(APIView):
    def get(self, request):
        inten = IntentMessages.objects.filter(id = views.ListInfo.id).values()
        print(views.ListInfo.id)
        intent = IntentMessagesSerializer(instance=inten, many=True)
        return Response(data=intent.data)
