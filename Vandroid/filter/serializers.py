
from rest_framework import serializers
from filter.models import Filter


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = "__all__"
