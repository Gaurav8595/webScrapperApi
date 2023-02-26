from .models import webData
from rest_framework import serializers

class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = webData
        fields = "__all__"
