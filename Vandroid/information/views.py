
from rest_framework.views import APIView
from rest_framework.response import Response
from information.models import Information
from information.serializers import InformationSerializer


class ListInfo(APIView):
    id = 0

    def post(self, request):
        info = Information.objects.filter(nameApp=request.data['nameApp']).values()
        info2 = InformationSerializer(instance=info, many=True)
        ListInfo.id = ((info2.data[0]['id']))
        return Response(data=info2.data)
