
from rest_framework import serializers
from activityComponents.models import ActivityComponents

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityComponents
        fields = "__all__"
