from rest_framework.views import APIView
from rest_framework.response import Response
from usesPermission.models import UsesPermission
from usesPermission.serializers import UsesPermissionSerializer
from information import views


class ListUsesPermission(APIView):
    def get(self, request):
        uses = UsesPermission.objects.filter(target_id=views.ListInfo.id).values()
        uses2 = UsesPermissionSerializer(instance=uses, many=True)
        return Response(data=uses2.data)
