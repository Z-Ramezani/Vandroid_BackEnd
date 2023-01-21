from rest_framework.views import APIView
from rest_framework.response import Response
from dynamicRegisteredComponents.models import DynamicRegisteredComponents
from dynamicRegisteredComponents.serializers import DynamicRegisteredSerializer
from information import views


class ListDynamicRegisteredComponents(APIView):
    def get(self, request):

        Dynam = DynamicRegisteredComponents.objects.filter(target_id=views.ListInfo.id).all()
        Dynamic = DynamicRegisteredSerializer(instance=Dynam, many=True)
        return Response(data=Dynamic.data)
