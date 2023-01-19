from rest_framework.views import APIView
from rest_framework.response import Response
from activityComponents.models import ActivityComponents
from activityComponents.serializers import ActivitySerializer
from information import views


class ListActivityComponents(APIView):
    def get(self, request):
        active = ActivityComponents.objects.filter(target_id=views.ListInfo.id).values()
        activity = ActivitySerializer(instance=active, many=True)
        ListActivityComponents.id = ((activity.data[0]['id']))
        return Response(data=activity.data)
