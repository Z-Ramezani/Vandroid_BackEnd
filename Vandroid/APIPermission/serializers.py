
from rest_framework import serializers
from APIPermission.models import APIPermission

class APIPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIPermission
        fields = "__all__"
