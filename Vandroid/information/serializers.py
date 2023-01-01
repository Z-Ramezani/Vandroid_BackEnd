from rest_framework import serializers

from information.models import Information


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"

# class InformationAppSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InformationApp
#         fields = "__all__"
