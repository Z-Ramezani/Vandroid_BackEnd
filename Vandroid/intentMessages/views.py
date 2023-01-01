from rest_framework.views import APIView
from rest_framework.response import Response
from intentMessages.models import IntentMessages
from intentMessages.serializers import IntentMessagesSerializer
from information import views

class ListIntentMessages(APIView):
    def get(self, request):
        inten = IntentMessages.objects.filter(target_id = views.ListInfo.id).values()
        intent = IntentMessagesSerializer(instance=inten, many=True)
        return Response(data=intent.data)
