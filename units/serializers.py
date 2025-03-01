from rest_framework import serializers
from .models import ConversionRule, ConversionHistory

class ConversionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversionRule
        fields = '__all__'

class ConversionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversionHistory
        fields = '__all__'