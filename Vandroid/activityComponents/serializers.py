

from rest_framework import serializers
from activityComponents.models import ActivityComponents, Filter

class FilterSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='categoryName')
    actions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='actionName')
    class Meta:
        model = Filter
        fields = ('name','actions', 'categories')


class ActivitySerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True, read_only=True)
    class Meta:
        model = ActivityComponents
        fields = ('target_id', 'exported', 'permissionName', 'filters')

