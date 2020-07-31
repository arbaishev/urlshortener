from rest_framework import serializers

from shortenerapp.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url', 'shortcode', 'updated', 'created', 'count']
