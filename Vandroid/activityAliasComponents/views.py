from rest_framework.views import APIView
from rest_framework.response import Response
from activityAliasComponents.models import ActivityAliasComponents
from activityAliasComponents.serializers import activityAliasSerializer
from information import views


class ListActivityAliasComponents(APIView):
    def get(self, request):
        alias = ActivityAliasComponents.objects.filter(target_id=views.ListInfo.id).values()
        alias2 = activityAliasSerializer(instance=alias, many=True)
        ListActivityAliasComponents.id = ((alias2.data[0]['id']))
        return Response(data=alias2.data)
