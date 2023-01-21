
from asyncore import read
from tkinter import TRUE
from rest_framework import serializers
from activityComponents.models import ActivityComponents


class ActivitySerializer(serializers.ModelSerializer):
    filters = serializers.SlugRelatedField(
        many=TRUE, read_only=True, slug_field='name')
    class Meta:
        model = ActivityComponents
        fields = ('target_id', 'exported', 'permissionName', 'filters')
