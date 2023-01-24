from rest_framework import serializers
from broadcastReceiversComponents.models import BroadcastReceiversComponents, Filter

class FilterSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='categoryName')
    actions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='actionName')
    class Meta:
        model = Filter
        fields = ('name','actions', 'categories')


class BroadcastReceiversSerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True, read_only=True)
    class Meta:
        model = BroadcastReceiversComponents
        fields = ('target_id', 'exported', 'permissionName','filterCheck','categoriesCheck', 'filters')

