from rest_framework import serializers

from .models import covidModel

class CovidSerializer(serializers.ModelSerializer):
    class Meta:
        model = covidModel
        fields = (
            'date',
            'origin',
            'sector',
            'gender'
        )

