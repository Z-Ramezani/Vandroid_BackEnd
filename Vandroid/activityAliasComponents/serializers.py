
from rest_framework import serializers
from activityAliasComponents.models import ActivityAliasComponents

class activityAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityAliasComponents
        fields = "__all__"
