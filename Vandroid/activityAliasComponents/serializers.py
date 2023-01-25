from rest_framework import serializers
from activityAliasComponents.models import ActivityAliasComponents, Filter


class FilterSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='categoryName')
    actions = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='actionName')

    class Meta:
        model = Filter
        fields = ('name', 'actions', 'categories')


class ActivityAliasSerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True, read_only=True)

    class Meta:
        model = ActivityAliasComponents
        fields = ('target_id','name','' 'exported', 'permissionName','categoriesCheck','filterCheck', 'filters')
