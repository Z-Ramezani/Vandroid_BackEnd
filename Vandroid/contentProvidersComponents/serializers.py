from rest_framework import serializers

from contentProvidersComponents.models import ContentProvidersComponents



class ContentProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentProvidersComponents
        fields = "__all__"
