
from rest_framework import serializers
from intentMessages.models import IntentMessages


class IntentMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntentMessages
        fields = "__all__"
