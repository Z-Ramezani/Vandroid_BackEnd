
from rest_framework import serializers
from customPermission.models import CustomPermission

class CustomPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPermission
        fields = "__all__"
