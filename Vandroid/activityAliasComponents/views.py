from rest_framework.views import APIView
from rest_framework.response import Response
from activityAliasComponents.models import ActivityAliasComponents
from activityAliasComponents.serializers import activityAliasSerializer
from information import views


class ListActivityComponents(APIView):
    def get(self, request):
        alias = ActivityAliasComponents.objects.filter(target_id=views.ListInfo.id).values()
        alias2 = activityAliasSerializer(instance=alias, many=True)
        return Response(data=alias2.data)
