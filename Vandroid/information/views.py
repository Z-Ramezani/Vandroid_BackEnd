
from rest_framework.views import APIView
from rest_framework.response import Response
from information.models import Information
from information.serializers import InformationSerializer
from rest_framework.generics import GenericAPIView


class ListInfo(GenericAPIView):
    id = 0
    data=""
    def post(self, request):

        info = Information.objects.filter(nameApp=request.data['nameApp']).values()
        info2 = InformationSerializer(instance=info, many=True)
        ListInfo.id = ((info2.data[0]['id']))
        ListInfo.data=info2.data
        return Response("done")
    def get(self,request):
        return Response(ListInfo.data)
