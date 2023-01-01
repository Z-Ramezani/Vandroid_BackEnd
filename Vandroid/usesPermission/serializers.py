
from rest_framework import serializers
from usesPermission.models import UsesPermission


class UsesPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsesPermission
        fields = "__all__"
