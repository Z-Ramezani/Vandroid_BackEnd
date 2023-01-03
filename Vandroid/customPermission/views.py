from rest_framework.views import APIView
from rest_framework.response import Response
from customPermission.models import CustomPermission
from customPermission.serializers import CustomPermissionSerializer
from information import views


class ListCustomPermission(APIView):
    def get(self, request):
        custom = CustomPermission.objects.filter(target_id=views.ListInfo.id).values()
        custom2 = CustomPermissionSerializer(instance=custom, many=True)
        return Response(data=custom2.data)
