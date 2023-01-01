from rest_framework.views import APIView
from rest_framework.response import Response
from customPermission.models import CustomPermission
from customPermission.serializers import CustomPermissionSerializer
from information import views


class ListCustomPermission(APIView):
    def get(self, request):
        inten = CustomPermission.objects.filter(
            target_id=views.ListInfo.id).values()
        intent = CustomPermissionSerializer(instance=inten, many=True)
        return Response(data=intent.data)
