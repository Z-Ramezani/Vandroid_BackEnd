from rest_framework.views import APIView
from rest_framework.response import Response
from broadcastReceiversComponents.serializers import BroadcastReceiversSerializer
from broadcastReceiversComponents.models import BroadcastReceiversComponents
from information import views


class ListBroadcastReceiversComponents(APIView):
    def get(self, request):

        bro = BroadcastReceiversComponents.objects.filter(target_id=views.ListInfo.id).all()
        Broad = BroadcastReceiversSerializer(instance=bro, many=True)
        return Response(data=Broad.data)
