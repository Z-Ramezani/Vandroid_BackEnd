
from rest_framework.views import APIView
from rest_framework.response import Response
from information.models import Information
from information.serializers import InformationSerializer


class ListInfo(APIView):
    id = 0

    def post(self, request):
        inf = Information.objects.filter(nameApp=request.data['nameApp']).values()
        info = InformationSerializer(instance=inf, many=True)
        ListInfo.id = ((info.data[0]['id']))
        return Response(data=info.data)
