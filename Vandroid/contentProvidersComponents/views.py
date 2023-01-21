from rest_framework.views import APIView
from rest_framework.response import Response
from contentProvidersComponents.models import ContentProvidersComponents
from contentProvidersComponents.serializers import ContentProvidersSerializer
from information import views



class ListContentProvidersComponents(APIView):
    def get(self, request):

        cont = ContentProvidersComponents.objects.filter(target_id=views.ListInfo.id).all()
        content = ContentProvidersSerializer(instance=cont, many=True)
        return Response(data=content.data)
