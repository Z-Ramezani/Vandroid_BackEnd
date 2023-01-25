from rest_framework import serializers
from servicesComponents.models import ServicesComponents, Filter


class FilterSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='categoryName')
    actions = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='actionName')

    class Meta:
        model = Filter
        fields = ('name','categoriesCheck', 'actions', 'categories')


class ServicesSerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True, read_only=True)

    class Meta:
        model = ServicesComponents
        fields = ('target_id','name','exported', 'permissionName','filterCheck', 'filters')
