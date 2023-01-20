from msilib.schema import Component
from rest_framework.views import APIView
from rest_framework.response import Response
from activityComponents import views
from activityAliasComponents import views
from servicesComponents import views
from information import views
from django.db.models import Q
from filter.models import Filter
from filter.serializers import FilterSerializer


class ListFilterComponents(APIView):
    def get(self, request):
        if Filter.componentName == "Activity":
            filt = Filter.objects.filter(Q(target_id_comp=views.ListActivityComponents.id))
        if Filter.componentName == "ActivityAlias":
            filt = Filter.objects.filter(Q(target_id_comp=views.ListActivityAliasComponents.id))
        if Filter.componentName == "ActivityAlias":
            filt = Filter.objects.filter(Q(target_id_comp=views.ListServicesComponents.id))
        filte = filt.values()
        filter = FilterSerializer(instance=filte, many=True)
        return Response(data=filter.data)
