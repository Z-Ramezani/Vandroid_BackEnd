from rest_framework.views import APIView
from rest_framework.response import Response
from activityComponents.models import ActivityComponents
from activityComponents.serializers import ActivityComponentsSerializer
from information import views


class ListActivityComponents(APIView):
    def get(self, request):
        active = ActivityComponents.objects.filter(target_id=views.ListInfo.id).values()
        activity = ActivityComponentsSerializer(instance=active, many=True)
        return Response(data=activity.data)
