
from rest_framework import serializers
from activityComponents.models import ActivityComponents

class ActivityComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityComponents
        fields = "__all__"
