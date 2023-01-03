from rest_framework.views import APIView
from rest_framework.response import Response
from APIPermission.models import APIPermission
from APIPermission.serializers import APIPermissionSerializer
from information import views


class ListAPIPermission(APIView):
    def get(self, request):
        APIPer = APIPermission.objects.filter(target_id=views.ListInfo.id).values()
        APIPerm = APIPermissionSerializer(instance=APIPer, many=True)
        return Response(data=APIPerm.data)
