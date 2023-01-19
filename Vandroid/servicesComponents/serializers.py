from rest_framework import serializers
from servicesComponents.models import ServicesComponents

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesComponents
        fields = "__all__"
