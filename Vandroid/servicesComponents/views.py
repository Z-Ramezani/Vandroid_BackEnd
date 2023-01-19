from rest_framework.views import APIView
from rest_framework.response import Response
from servicesComponents.models import ServicesComponents
from servicesComponents.serializers import ServicesSerializer
from information import views


class ListServicesComponents(APIView):
    def get(self, request):
        active = ServicesComponents.objects.filter(target_id=views.ListInfo.id).values()
        activity = ServicesSerializer(instance=active, many=True)
        return Response(data=activity.data)
